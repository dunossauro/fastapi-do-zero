---
marp: true
theme: rose-pine
---

# Tornando o projeto assíncrono

> https://fastapidozero.dunossauro.com/4.0/08/

---

## Objetivos da Aula


- Introduzir os conceitos de programação assíncrona
- Refatorar nossa aplicação para suportar AsyncIO
  - Tanto a aplicação (SQLAlchemy, FastAPI)
  - Quanto os testes (Pytests, Fixtures)

---

## O bloqueio da aplicação

> Parte 1

---

## Bloqueio de I/O

Um dos problemas mais comuns ao lidarmos com uma aplicação web é a necessidade de estarmos sempre disponíveis para responder a requisições enviadas pelos clientes. Quando recebemos uma requisição, normalmente precisamos processá-la:

<div class="mermaid">
graph LR
    A["Validar o schema"] --> B["Conectar ao DB"]
	B --> C["Fazer algumas operações"]
	C --> D["Repassa ao banco de dados"]
	D --> E["Retornar o recurso"]
	subgraph B1[aguardando I/O]
    B
    end
	subgraph B2[aguardando I/O]
    D
    end
</div>

Esse fluxo de execução é chamado de **bloqueante**, pois a aplicação fica "parada", aguardando a resposta de sistemas externos, como o banco de dados.

---

## Bloqueio de I/O

<div class="columns">

<div>

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
    try:
        current_user.username = user.username
        current_user.password = get_password_hash(user.password)
        current_user.email = user.email
        session.commit()
        session.refresh(current_user)

        return current_user

    except IntegrityError:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail='Username or Email already exists',
        )
```

</div>

<div class="mermaid">
graph TD
    A["Validar o schema"] --> B1
	B1 --> C["Algumas operações"]
	C --> B2
	C --> E["Retornar o recurso"]
	subgraph B1[aguardando I/O]
    B["Conectar ao DB"]
    end
	subgraph B2[aguardando I/O]
    D["Repassa ao banco de dados"]
    end
	B2 --> C
</div>

</div>

---

## O bloqueio é da **aplicação**

Uma coisa que deve ficar **extremamente clara** é que embora tenhamos um bloqueio na aplicação, **não** temos um bloqueio no **servidor** (uvicorn).

<div class="mermaid">
	flowchart LR
	   Cliente_1 --> Uvicorn
	   Cliente_2 --> Uvicorn
	   Cliente_3 --> Uvicorn
	   Uvicorn --> Backlog
	   Backlog --> Uvicorn
	   Uvicorn --> APP
	   APP --> Uvicorn
</div>

Por padrão, são `2048` requisições que podem aguardar no backlog

---

## O servidor pode "copiar" a aplicação

Com isso distribuir as requisições de forma paralela

<div class="mermaid">
	flowchart LR
	   Cliente --> Uvicorn
	   Uvicorn --> copia_01
	   Uvicorn --> copia_02
	   Uvicorn --> copia_03
</div>

```bash
uvicorn fast_zero.app:app --workers 3
```

A aplicação ainda bloqueia, mas como tem mais, faz coisas ao mesmo tempo.

---

## Aplicação **não** bloqueante

> Parte 2

---

## Corrotinas

Embora esse assunto possa se estender de forma sem controle, uma corrotina *assíncrona* basicamente é uma função em python que pode ser **escalonada** durante o bloqueio de I/O.

São criadas pela palavra reservada `async` e o escalonamento é feito pela palavra `await`.


```python
# código ilustrativo ao nosso contexto
async def get_users() -> list[User]:
    result = await session.scalars(select(User))
    return result
```

---

## Corrotinas

Uma das características de uma corrotina, é o fato dela não ser executada quando chamada diretamente:

```python
>>> async def foo():
...     ...
...
>>> foo()
<coroutine object foo at 0x7f2e0ec79850>
```

Ela precisa ser executada por um agente externo. Um **loop de eventos**.

---

## Loop de eventos

É responsável por executar e coordenar todas as corrotinas. Sempre que precisamos de cooperação entre os bloqueios, o loop ficará responsável por executar as corrotinas e nos trazer o resultado.

> TODO

---

## Cooperatividade e Escalonamento

> TODO

---

## Bando de dados e bloqueios

> Parte 3

---

## Instalando o suporte a asyncio no sqla

Embora o suporte a `asyncio` seja nativo no `sqlalchemy` 2.0. Algumas plataformas (como Silicon) não tem os pacotes pré-compilados (wheels) do `greenlet`. Para isso, vamos fazer uma instalação explícita:

```bash
poetry add "sqlalchemy[asyncio]"
```

> obs: A partir da versão 2.1, o suporte a asyncio deverá **sempre** ser instalado manualmente!

---

## SQLite + AsyncIO

Como estamos utilizando o banco de dados SQLite, que não possui suporte nativo a asyncio no Python, precisamos instalar uma extensão chamada aiosqlite. Ela permite a execução assíncrona com bancos SQLite:

```bash
poetry add aiosqlite
```

---

## Alterando o `.env`

Para que nossa conexão esteja ciente que o aiosqlite está sendo usado, devemos alterar a variável de ambiente para contemplar essa alteração:

```bash
DATABASE_URL="sqlite+aiosqlite:///database.db"
```

---

## Sessão com suporte a AsyncIO

```python
#fast_zero/database.py
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from fast_zero.settings import Settings

engine = create_async_engine(Settings().DATABASE_URL)


async def get_session():
    async with AsyncSession(engine, expire_on_commit=False) as session:
        yield session
```

`expire_on_commit` deve ser `False` pois não sabemos se todas as corrotinas "liberaram" a sessão. Para prevenir erros, essa opção de ser ativada.

---

## Pytest + AsyncIO

Embora o SQLAlchemy e o FastAPI lidem de forma nativa com programação assíncrona, o pytest ainda não. Para isso, precisamos instalar uma extensão que adicione esse suporte. A pytest-asyncio fornece um mecanismo de marcação para testes e também um para criação de fixtures assíncronas:

```bash
poetry add --group dev pytest-asyncio
```

---

## Pytest + AsyncIO

Uma exigência formal do pytest-asyncio é que seja configurado o escopo padrão das fixtures:

```toml
[tool.pytest.ini_options]
pythonpath = "."
addopts = '-p no:warnings'
asyncio_default_fixture_loop_scope = 'function'
```

> Para evitar cair em mais um assunto, o tópico de escopos de fixtures serão abordados na aula 11

---

## Fixture async para `session`

```python
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

@pytest_asyncio.fixture 
async def session():
    engine = create_async_engine(
        'sqlite+aiosqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    # ...
```

---

## Fixture async para `session`

```python
@pytest_asyncio.fixture 
async def session():
    # ...
    async with engine.begin() as conn: 
        await conn.run_sync(table_registry.metadata.create_all) 

    async with AsyncSession(engine, expire_on_commit=False) as session:
        yield session

    async with engine.begin() as conn:
        await conn.run_sync(table_registry.metadata.drop_all)
```

---

## Testando o banco de dados

```python
#tests/test_db.py
import pytest

@pytest.mark.asyncio 
async def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username='alice', password='secret', email='teste@test'
        )
        session.add(new_user)
        await session.commit() 

    user = await session.scalar(select(User).where(User.username == 'alice')) 
    # ...
```

--- 

## Rodando um único arquivo

```bash
task test tests/test_db.py
```

---


## Refatorando com teste!

> Parte 4

---

## Técnica de refatoração com testes

Uma das grandes vantagens de termos uma boa cobertura de testes é que podemos fazer mudanças estruturais no projeto e garantir que tudo funcione da forma como já estava antes. Os testes nos trazem uma **segurança** para que tudo possa mudar internamente sem alterar os resultados da API. Para isso, a estratégia que vamos usar aqui é a de caminhar executando um teste por vez.

---

Uma das funcionalidades legais do pytest é poder executar somente um único teste, ou um grupo deles, usando o nome do teste como base. Para isso, podemos chamar task test passando a flag `-k` seguida do nome do teste. Algo como:


```bash
task test -k test_create_user

# ...
tests/test_users.py::test_create_user FAILED
```

Para cada teste que falhar, vamos nos organizando para fazer a conversão do código para assíncrono.

---

Para listar todos os testes presentes no nosso projeto, podemos usar a flag `--collect-only` do pytest:

```bash
task test --collect-only
<Dir fast_zero>
  <Package tests>
    <Module test_app.py>
      <Function test_root_deve_retornar_ok_e_ola_mundo>
    <Module test_auth.py>
      <Function test_get_token>
    <Module test_db.py>
      <Coroutine test_create_user>
...
```

---

## Suplementar / Para próxima aula

Na próxima aula, vamos adicionar randomização em testes para facilitar a criação dos dados de teste. Caso não conheça o Faker ou Factory-boy, pode ser uma boa para entender melhor a próxima aula:

- [Randomização de dados em testes unitários com Faker e Factory-boy | Live de Python #281](https://youtu.be/q_P-2h5L1cE){:target="_blank"}

---

## Exercícios e Quiz

1. Reveja os endpoints criados por você em exercícios anteriores e adicione async e await para que eles se tornem não bloqueantes também.
2. Altere o endpoint read_root para suportar asyncio.

> Não esqueça de responder o [quiz](https://fastapidozero.dunossauro.com/4.0/quizes/aula_08/)

---

## Commit

```bash
git add .
git commit -m "Refatorando estrutura do projeto: Suporte a asyncio, tornando o projeto não bloqueante"
```

<!-- mermaid.js -->
<script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"></script>
<script>mermaid.initialize({startOnLoad:true,theme:'dark'});</script>
