---
marp: true
theme: rose-pine
style: |
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
---

# Integrando Banco de Dados a API

> https://fastapidozero.dunossauro.com/04/

---

## Objetivos dessa aula:

- Integrando SQLAlchemy à nossa aplicação FastAPI
- Utilizando a função Depends para gerenciar dependências
- Modificando endpoints para interagir com o banco de dados
- Testando os novos endpoints com Pytest e fixtures

---

# Integrando SQLAlchemy à Nossa Aplicação FastAPI

A peça principal da nossa integração é a **sessão** do ORM. Ela precisa ser visível aos endpoints para que eles possam se comunicar com o banco.

<div class="mermaid" style="text-align: center;">
graph LR
  Enpoint <--> Session
  Session <--> id1[(Database)]
</div>

---

# Sessão

Uma peça chave do SQLAlchemy é o conceito de uma "sessão". Se você é novo no mundo dos bancos de dados, pode pensar na sessão como um carrinho de compras virtual: conforme você navega pelo site (ou, neste caso, conforme seu código executa), você pode adicionar ou remover itens desse carrinho. No entanto, nenhuma alteração é realmente feita até que você decida finalizar a compra. No contexto do SQLAlchemy, "finalizar a compra" é equivalente a fazer o commit das suas alterações.

---

1. **Repositório**: A sessão atua como um repositório. A ideia de um repositório é abstrair qualquer interação envolvendo persistência de dados.

3. **Unidade de Trabalho**: Cada objeto adicionado ou removido da sessão é reconhecido como uma **unidade**. Fazendo com que possam ser removidos ou adicionados na sessão ter intervir na conexão com o banco. 

2. **Mapeamento de Identidade**: É criado um cache para as entidades que já estão carregadas na sessão para evitar conexões desnecessárias.

---

# De uma forma visual

<div class="mermaid" style="text-align: center;">
graph
  Enpoint --> Session
  Session --> scalars
  Session --> scalar
  scalar --> Busca_Dado[Busca um dado]
  scalars --> Busca_Dados[Busca N dados]
  Session --> add
  add --> ADD[Adiciona/Deleta um objeto]
  Session --> delete
  delete --> ADD[Adiciona/Deleta um objeto]
  Session --> rollback
  rollback --> D[Desfaz a UT]
  Session --> commit
  commit --> DB[DB / executa UTs]
</div>

---

## Criando a nossa sessão


```python
# fast_zero/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fast_zero.settings import Settings

engine = create_engine(Settings().DATABASE_URL)


def get_session():
    with Session(engine) as session:
        yield session
```

---

## Gerenciando Dependências com FastAPI

Assim como a sessão SQLAlchemy, que implementa vários padrões arquiteturais importantes, FastAPI também usa um conceito de padrão arquitetural chamado "Injeção de Dependência".

FastAPI fornece a função `Depends` para ajudar a declarar e gerenciar essas dependências. É uma maneira declarativa de dizer ao FastAPI: "Antes de executar esta função, execute primeiro essa outra função e passe-me o resultado". Isso é especialmente útil quando temos operações que precisam ser realizadas antes de cada request, como abrir uma sessão de banco de dados. 

---

<div class="columns">

<div class="mermaid" style="text-align: center;">
graph LR
   código -- depende de --> sessão
  subgraph Função
  código
  end
</div>

<div>

```python
def endpoint(
    user: UserSchema,
    session = Depends(get_session)
):

    session...
```
</div>

</div>

---

## Implementando o banco nos endpoints

```python
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

# ...

@app.post('/users/', response_model=UserPublic, status_code=201)
def create_user(user: UserSchema, session: Session = Depends(get_session)):
    db_user = session.scalar(
        select(User).where(User.username == user.username)
    )
    if db_user:
        raise HTTPException(
            status_code=400, detail='Username already registered'
        )
    # ...
```

---

## Criando uma estrutura para usar a sessão de testes


```python
# tests/conftest.py
@pytest.fixture
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()
```

---

## Alterando nosso teste

```python
def test_create_user(client):
    response = client.post(
        '/users',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == 201
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }
```

---

## Erros!

A fixture precisa de algumas pequenas adaptações para rodar em threads diferentes:

```python
@pytest.fixture
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    yield Session()

    Base.metadata.drop_all(engine)
```

---

# Implementação dos outros endpoints

...

---

# Commit!

```shell title="$ Execução no terminal!"
git add .
git commit -m "Atualizando endpoints para usar o banco de dados real"
git push
```

<!-- mermaid.js -->
<script src="https://unpkg.com/mermaid@10.4.0/dist/mermaid.min.js"></script>
<script>mermaid.initialize({startOnLoad:true,theme:'dark'});</script>
