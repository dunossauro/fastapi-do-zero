---
marp: true
theme: rose-pine
---

# Tornando o sistema de autenticação robusto

> https://fastapidozero.dunossauro.com/08/

---

## Objetivos da Aula

- Testar os casos de autenticação de forma correta
- Testar os casos de autorização de forma correta
- Implementar o refresh do token
- Introduzir testes que param o tempo com `freezegun`
- Introduzir geração de modelos automática com `factory-boy`

---

# Testes de autorização

> Parte 1

---

## Garantir que o user faça somente o que pode

```python
@router.put('/{user_id}', response_model=UserPublic)
def update_user(
    user_id: int,
    user: UserSchema,
    session: Session,
    current_user: CurrentUser,
):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN,
            detail='Not enough permissions'
        )
```

Não deve ser possível alterar via PUT os dados que não são seus

---

```python
def test_update_user_with_wrong_user(client, user, token):
    response = client.put(
        f'/users/{user.id + 1}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'Not enough permissions'}
```

Na ultima aula fizemos algo parecido com isso!


---

## O problema dessa abordagem

O uso do `+1` nos leva a algumas discussões interessantes:

- Validamos a situação com um "hack", não existe o `+1`
- Caso ele exista, o que vai acontecer em produção, vai funcionar?
- Como representamos um cenário mais próximo da realidade?
* **precisamos adicionar um novo user ao cenário de teste**

---

## Criando modelos `Users` sob demanda

Para fazer a criação de users de forma mais intuitiva e sem a preocupação de valores repetidos, podemos usar uma "**fábrica**" de usuários.

Isso pode ser feito com uma biblioteca chamada `factory-boy`:

```shell
poetry add --group dev factory-boy
```

> Fábrica é um padrão de projeto de construção de objetos.

---

## O Factory-boy

```python
#conftest.py
import factory

# ...

class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'test{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@test.com')
    password = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')
```

---

## O uso do factory-boy + fixture

<div class="columns">

<div>

Aplicando a fabrica:

```python
@pytest.fixture
def user(session):
    password = 'testtest'
    user = UserFactory(
        password=get_password_hash(password)
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    user.clean_password = 'testtest'

    return user
```

</div>

<div>

O cenário "real":

```python
@pytest.fixture
def other_user(session):
    password = 'testtest'
    user = UserFactory(
        password=get_password_hash(password)
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    user.clean_password = 'testtest'

    return user
```

</div>

</div>

---


## Alterando o teste de put para esse cenário

```python
def test_update_user_with_wrong_user(client, other_user, token):
    response = client.put(
        f'/users/{other_user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'Not enough permissions'}
```


---

## Criando um teste de DELETE para o cenário

```python
def test_delete_user_wrong_user(client, other_user, token):
    response = client.delete(
        f'/users/{other_user.id}',
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'Not enough permissions'}
```

---

# Expiração do token

> Parte 2

---

## Sobre o tempo do token

TODO:

- Claim exp
- ExpiredSignatureError
- freezegun

---

# Problemas de autenticação

> Parte 4

---

TODO:

- Senha incorreta
- Email inexistente

---

# Refresh do token

> Parte 5

---

TODO:

- Implementar o código
- Implementar o teste

---

# Quiz

Não esqueça de responder o [quiz](https://fastapidozero.dunossauro.com/quizes/aula_08/) dessa aula!

---

# Commit

```shell
git add .
git commit -m "Implementando o reresh do token e testes de autorização"
```
