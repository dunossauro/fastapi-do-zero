# Exercícios da aula 05

## Exercício 01
Escrever um teste para o endpoint de POST (create_user) que contemple o cenário onde o username já foi registrado. Validando o erro `#!python 409`.

### Solução

Para testar esse cenário, precisamos de um username que já esteja registrado na base de dados. Para isso, podemos usar a fixture de `user` que criamos. Ela é uma garantia que o valor já está inserido no banco de dados:

```py title="/tests/test_app.py" hl_lines="1 5"
def test_create_user_should_return_409_username_exists__exercicio(client, user):
    response = client.post(
        '/users/',
        json={
            'username': user.username,
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'Username already exists'}
```

## Exercício 02
Escrever um teste para o endpoint de POST (create_user) que contemple o cenário onde o e-mail já foi registrado. Validando o erro `#!python 409`.

### Solução

Para testar esse cenário, precisamos de um e-mail que já esteja registrado na base de dados. Para isso, podemos usar a fixture de `user` que criamos. Ela é uma garantia que o valor já está inserido no banco de dados:

```py title="/tests/test_app.py" hl_lines="1 5"
def test_create_user_should_return_409_email_exists__exercicio(client, user):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': user.email,
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'Email already exists'}
```

## Exercício 03

Atualizar os testes criados nos exercícios 1 e 2 da [aula 03](../03.md/#exercicios){:target="_blank"} para suportarem o banco de dados.

### Solução

O objetivo desse exercício não necessariamente uma atualização dos testes, mas o caso de uma execução para validar se os testes, como foram feitos ainda funcionariam nessa nova estrutura.

Os meus testes da aula 03:

```python
def test_delete_user_should_return_not_found__exercicio(client):
    response = client.delete('/users/666')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user_should_return_not_found__exercicio(client):
    response = client.put(
        '/users/666',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
```

Ao executar eles continuam passando.

## Exercício 04

Implementar o banco de dados para o endpoint de listagem por id, criado no exercício 3 da [aula 03](../03.md/#exercicios){:target="_blank"}.


### Solução

Esse exercício basicamente consiste em duas partes. A primeira é alterar o endpoint para usar o banco de dados. Isso pode ser feito de maneira simples injetando a dependência da `session`:

```python
@app.get('/users/{user_id}', response_model=UserPublic)
def read_user__exercicio(
    user_id: int, session: Session = Depends(get_session)
):
    db_user = session.scalar(select(User).where(User.id == user_id))

    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    return db_user
```

A segunda parte é entender o que precisa ser feito nos testes para que eles consigam cobrir os dois casos previstos. O de sucesso e o de falha.

O teste de sucesso continua passando, pois ele de fato não depende de nenhuma interação com o banco de dados:
```python
def test_get_user_should_return_not_found__exercicio(client):
    response = client.get('/users/666')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
```

Já o teste de sucesso, depende que exista um usuário na base dados. Com isso podemos usar a fixture de `user` tanto na chamada, quanto na validação dos dados:

```python
def test_get_user___exercicio(client, user):
    response = client.get(f'/users/{user.id}')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': user.username,
        'email': user.email,
        'id': user.id,
    }
```
