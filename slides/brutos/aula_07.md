---
marp: true
theme: rose-pine
---

# Refatorando a Estrutura do Projeto

> https://fastapidozero.dunossauro.com/07/

---

## Objetivos da Aula

- **Reestruturar o projeto para facilitar sua manutenção**
- Mover coisas de altenticação para um arquivo chamado `fast_zero/auth.py`
- Deixando em `fast_zero/secutiry.py` somente as validações de senha
- Remover constantes do código
- Criar routers específicos
- Testes

---

# Parte 1

Routers

---

## Routers

O FastAPI nos fornece um recurso útil chamado routers:

- Nos permite organizar e agrupar diferentes rotas em nossa aplicação.
- Organização por domínios
- Um "subaplicativo" FastAPI que pode ser montado em uma aplicação principal.

Ao usar routers, podemos manter nosso código mais organizado e legível, especialmente à medida que nossa aplicação cresce e adicionamos mais rotas.

---

### Criando um router para Users

A ideia é mover tudo que é referente a users para um arquivo único que vamos chamar de `fast_zero/routes/users.py`

```python
from fastapi import APIRouter

# imports ...

router = APIRouter(prefix='/users', tags=['users'])
```

- `prefix`: o prefixo adiciona o `/users` em todos os endpoints do router
- `tags`: agrupa os endpoints na documentação

---

### Implementando as rotas

Temos que alterar nossos endpoints. Agora o decorador deixa de ser `@app` e vira `@router`. Como já criamos os prefixos, as URLs não precisam mais iniciar com `/users`

```python
@router.post('/', response_model=UserPublic, status_code=201)
@router.get('/', response_model=UserList)
@router.put('/{user_id}', response_model=UserPublic)
@router.delete('/{user_id}', response_model=Message)
```

---

## Um router para Auth

```python
from fastapi import APIRouter

# outros imports

router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/token', response_model=Token)
def login_for_access_token(form_data: OAuth2Form, session: Session):
    #...
```

---

# Juntando os routers no APP

```python
from fastapi import FastAPI

from fast_zero.routes import auth, users

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}
```

---

# Uma pausa para acessar o swagger agora!

> http://localhost:8000

---

# Outra pausa para rodar os testes

E ver se tudo continua indo bem!

```shell
task test
```

---

# Um pequeno problema

Como inserimos o prefixo no router de autorização, a url para acessar o token também mudou. Foi de `/token` para `/auth/token`, isso precisa ser contemplado no redirecionamento do Bearer token do JWT.

> Mostrar o erro no [swagger](localhost:8000/docs)

---

# Validação do token

Para corrigir o redirecionamento, precisamos alterar o objeto `OAuth2PasswordBearer` em `security.py`

```python
# security.py
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/token')
```

---

# Parte 2

Reestruturando os testes

---

## Criando novos arquivos

Da mesma forma que dividimos as responsabilidades do app nos routers, também podemos deixar nossos arquivos de teste mais simples.

- `/tests/test_app.py`: Para testes relacionados ao aplicativo em geral
- `/tests/test_auth.py`: Para testes relacionados à autenticação e token
- `/tests/test_users.py`: Para testes relacionados às rotas de usuários

---

# Claro, precisamos executar os testes de novo

```shell
task test
```

---

# SIM, eles não funcionam

> Mas por que???

---

### Ajustando a fixture de `token`

A alteração da fixture de `token` é igual que fizemos em `/tests/test_auth.py`, precisamos somente corrigir o novo endereço do router no arquivo `/tests/conftest.py`:

```python
@pytest.fixture
def token(client, user):
    response = client.post(
        '/auth/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    return response.json()['access_token']
```

Fazendo assim com que os testes que dependem dessa fixture passem a funcionar.


---

# Parte 3

Usando o tipo `Annotated` para simplificar definições

---

# O tipo Annotated

O FastAPI suporta um recurso fascinante da biblioteca nativa `typing`, conhecido como `Annotated`. Esse recurso prova ser especialmente útil quando buscamos simplificar a utilização de dependências.

Ao definir uma anotação de tipo, seguimos a seguinte formatação: `nome_do_argumento: Tipo = Depends(o_que_dependemos)`. Em todos os endpoints, acrescentamos a injeção de dependência da sessão da seguinte forma:

```python
session: Session = Depends(get_session)
```

---

# O tipo Annotated

O tipo `Annotated` nos permite combinar um tipo e os metadados associados a ele em uma única definição. Através da aplicação do FastAPI, podemos utilizar o `Depends` no campo dos metadados. Isso nos permite encapsular o tipo da variável e o `Depends` em uma única entidade, facilitando a definição dos endpoints.

Veja o exemplo a seguir:

```python
from typing import Annotated

Session = Annotated[Session, Depends(get_session)]
CurrentUser = Annotated[User, Depends(get_current_user)]
```

---

### Simplificando Users

```python
@router.post('/', response_model=UserPublic, status_code=201)
def create_user(user: UserSchema, session: Session):
# ...

@router.get('/', response_model=UserList)
def read_users(session: Session, skip: int = 0, limit: int = 100):
# ...

@router.put('/{user_id}', response_model=UserPublic)
def update_user(
    user_id: int,
    user: UserSchema,
    session: Session,
    current_user: CurrentUser
):
# ...

@router.delete('/{user_id}', response_model=Message)
def delete_user(user_id: int, session: Session, current_user: CurrentUser):
# ...
```

---

### Simplificando Auth

```python
from typing import Annotated

# ...

OAuth2Form = Annotated[OAuth2PasswordRequestForm, Depends()]
Session = Annotated[Session, Depends(get_session)]

@router.post('/token', response_model=Token)
def login_for_access_token(form_data: OAuth2Form, session: Session):
#...
```

---

# Claro, precisamos executar os testes de novo

```shell
task test
```

---
# Parte 4

Movendo as constantes para variáveis de ambiente

---

### O problema com os 12 fatores

```python
SECRET_KEY = 'your-secret-key'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
```

Estes valores não devem estar diretamente no código-fonte, então vamos movê-los para nossas variáveis de ambiente e representá-los na nossa classe `Settings`.

---

### Adicionando as constantes a Settings

```python
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )

    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
```

---

### Adicionando estes valores ao nosso arquivo `.env`.


```shell
DATABASE_URL="sqlite:///database.db"
SECRET_KEY="your-secret-key"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Com isso, podemos alterar o nosso código em `zero_app/security.py` para ler as constantes a partir da classe `Settings`.

---

## Alterando o arquivo de security


```python
from fast_zero.settings import Settings

settings = Settings()
```

```python title="zero_app/security.py"
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt
```

---

# Claro, precisamos executar os testes de novo

```shell
task test
```

---

# Exercicio e quiz

Migre os endpoints e testes criados nos exercícios anteriores para os locais corretos na nova estrutura da aplicação.

> Não esqueça de responder o [quiz](https://fastapidozero.dunossauro.com/quizes/aula_07/)

---

# Commit!

```shell
git add .
git commit -m "Refatorando estrutura do projeto
- Criado routers para Users e Auth
- Movendo constantes para variáveis de ambiente."
```
