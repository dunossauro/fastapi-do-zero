# Exercícios da aula 06

## Exercício 01

Faça um teste para cobrir o cenário que levanta exception `credentials_exception` na autenticação caso o `email` não seja enviado via JWT. Ao olhar a cobertura de `security.py` você vai notar que esse contexto não está coberto.

### Solução

Para executar o bloco de código você deve fazer uma chamada a qualquer endpoint que dependa do token (currentUser) e enviar um token que não contenha um endereço de e-mail (sub):

```python title="tests/test_app.py"
def test_get_current_user_not_found__exercicio(client):
    data = {'no-email': 'test'}
    token = create_access_token(data)

    response = client.delete(
        '/users/1',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}
```

## Exercício 02

Faça um teste para cobrir o cenário que levanta exception `credentials_exception` na autenticação caso o email seja enviado, mas não exista um `User` correspondente cadastrado na base de dados. Ao olhar a cobertura de `security.py` você vai notar que esse contexto não está coberto.

### Solução

Para executar o bloco de código você deve fazer uma chamada a qualquer endpoint que dependa do token (currentUser) e enviar um token que contenha um endereço de email (sub) que não esteja cadastrado na base de dados:

```python title="tests/test_app.py"
def test_get_current_user_does_not_exists__exercicio(client):
    data = {'sub': 'test@test'}
    token = create_access_token(data)

    response = client.delete(
        '/users/1',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}
```

## Exercício 03

Reveja os testes criados até a aula 5 e veja se eles ainda fazem sentido (testes envolvendo `#!python 400`)

### Solução

Os testes para os endpoints de PUT e DELETE, que verificam usuários não existentes na base de dados não fazem mais sentido. Já que para alterar ou deletar um user, você tem que ser validado pelo token. Esses testes podem ser deletados.
