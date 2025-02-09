# Exercícios da aula 08

## Exercício 01

O endpoint de `PUT`usa dois users criados na base de dados, porém, até o momento ele cria um novo user no teste via request na API por falta de uma fixture como `other_user`. Atualize o teste para usar essa nova fixture.


### Solução

Para resolver esse exercício você só precisa remover a chamada para API e fazer com que o 'username' do PUT seja o de `other_user`:

```python title="tests/test_users.py"
def test_update_integrity_error(client, user, other_user, token):
    response_update = client.put(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': other_user.username,
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )

    assert response_update.status_code == HTTPStatus.CONFLICT
    assert response_update.json() == {
        'detail': 'Username or Email already exists'
    }
```
