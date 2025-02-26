# Exercícios da aula 03

## Exercício 01

Escreva um teste para o erro de `#!python 404` (NOT FOUND) para o endpoint de PUT.

### Solução

A ideia de um teste de `#!python 404` para o PUT é **tentar** fazer a alteração de um usuário que não existe no banco de dados.

```python title="Teste de 404"
def test_update_user_should_return_not_found__exercicio(client):
    response = client.put(
        '/users/666', #(1)!
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND #(2)!
    assert response.json() == {'detail': 'User not found'} #(3)!
```

1. O user com id `#!python 666` não existe no nosso sistema.
2. Como o user não existe, o status code retornado pela função será `#!python 404`
3. Por entrar no bloco de validação do `if` o `HTTPException` foi preenchido com `detail='User not found'`

## Exercício 02

Escreva um teste para o erro de `#!python 404` (NOT FOUND) para o endpoint de DELETE

### Solução

A ideia de um teste de 404 para o DELETE é **tentar** fazer a alteração de um usuário que não existe no banco de dados.

```python title="Teste de 404"
def test_delete_user_should_return_not_found__exercicio(client):
    response = client.delete('/users/666') #(1)!

	assert response.status_code == HTTPStatus.NOT_FOUND #(2)!
    assert response.json() == {'detail': 'User not found'} #(3)!
```

1. O user com id `#!python 666` não existe no nosso sistema.
2. Como o user não existe, o status code retornado pela função será `#!python 404`
3. Por entrar no bloco de validação do `if` o `HTTPException` foi preenchido com `detail='User not found'`



## Exercício 03

Adicionar uma chamada de log para o endpoint de DELETE e escrever um teste para ele

### Solução

A alteração no código:

```python hl_lines="4"
@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        logger.info(f'User with {user_id=} not found in the database')
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    del database[user_id - 1]

    return {'message': 'User deleted'}
```

O teste para o log:

```python
def test_delete_user_should_log_not_found__exercicio(client, caplog):
    caplog.set_level(INFO)
    client.delete('/users/666')

    _, level, msg = caplog.record_tuples[0]
    assert level == INFO
    assert msg == 'User with user_id=666 not found in the database'
```

## Exercício 04

Crie um endpoint de GET para pegar um único recurso como `users/{id}` e fazer seus testes para `#!python 200` e `#!python 404` (os logs devem ser incluídos).

### Solução

A implementação do endpoint é bastante parecida com as que fizemos até agora. Precisamos validar se existe um `id` comparível no nosso banco de dados falso. Nos baseando pela posição do elento na lista.

```python
@app.get('/users/{user_id}', response_model=UserPublic)
def read_user__exercicio(user_id: int):
    if user_id > len(database) or user_id < 1:
        logger.info(f'User with {user_id=} not found in the database')
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    return database[user_id - 1]
```

Um dos testes é sobre o retorno `#!python 404`, que é retornado um user que não existe na base de dados e outro é o comportamento padrão para quando o user é retornado com sucesso:

```python
def test_get_user_should_return_not_found__exercicio(client):
    response = client.get('/users/666')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_get_user___exercicio(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_get_user_should_log_not_found__exercicio(client, caplog):
    caplog.set_level(INFO)
    client.get('/users/666')

    _, level, msg = caplog.record_tuples[0]
    assert level == INFO
    assert msg == 'User with user_id=666 not found in the database'
```
