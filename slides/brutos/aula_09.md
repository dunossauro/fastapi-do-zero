---
marp: true
theme: rose-pine
---

# Criando Rotas CRUD para Gerenciamento de Tarefas em FastAPI

> https://fastapidozero.dunossauro.com/09/

---

## Objetivos da Aula


- Criação das rotas para as operações CRUD das tarefas
- Fazer com só o usuário dono da tarefa possa acessar e modificar suas tarefas
- Escrita e execução dos testes para cada operação das tarefas

---

# Como funciona um todo list?

> https://selenium.dunossauro.com/todo_list.html

---

## Vamos por partes :)

1. Um novo router para tarefas
2. Uma nova tabela no banco
3. Novos schemas para tarefas
4. Novos endpoints para tarefas

---

# O primeiro endpoint

> Parte 1

---

Vamos criar um novo router para os todos em `fast_zero/routers/todos.py`

```python
from fastapi import APIRouter

router = APIRouter(prefix='/todos', tags=['todos'])
```

E linkar ele:

```python
from fast_zero.routers import auth, todos, users
from fast_zero.schemas import Message

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(todos.router)
```

---

## Nosso primeiro endpoint

Um endpoint de criação de todos

```python
@router.post('/', response_model=???)
def create_todo(todo: ???):
    return ???
```

---

## Mas e os schemas?

<div class="columns">

<div>

```python
# schemas.py
from fast_zero.models import TodoState
# ...
class TodoSchema(BaseModel):
    title: str
    description: str
    state: TodoState
	
class TodoPublic(BaseModel):
    id: int
    title: str
    description: str
    state: TodoState
```

</div>

<div>

```python
# models.py
from enum import Enum
# ...
class TodoState(str, Enum):
    draft = 'draft'
    todo = 'todo'
    doing = 'doing'
    done = 'done'
    trash = 'trash'
```

</div>

</div>


---

## De volta ao endpoint

```python
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from fast_zero.database import get_session
from fast_zero.models import User
from fast_zero.schemas import TodoPublic, TodoSchema
from fast_zero.security import get_current_user

router = APIRouter(prefix='/todos', tags=['todos'])

Session = Annotated[Session, Depends(get_session)]
CurrentUser = Annotated[User, Depends(get_current_user)]


@router.post('/', response_model=TodoPublic)
def create_todo(
    todo: TodoSchema,
    user: CurrentUser,
    session: Session,
):
    return todo
```

---

## A tabela no banco de dados

> Parte 2

---

## A tabela e seu relacionamento

```python
from sqlalchemy import ForeignKey, func
# ...
@table_registry.mapped_as_dataclass
class Todo:
    __tablename__ = 'todos'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    state: Mapped[TodoState]

    # Toda tarefa pertence a alguém
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
```

---

## Juntando o endpoint com o banco de dados

```python {1,3}
from fast_zero.models import Todo, User
# ...
@router.post('/', response_model=TodoPublic)
def create_todo(
    todo: TodoSchema,
    user: CurrentUser,
    session: Session,
):
    db_todo = Todo(
        title=todo.title,
        description=todo.description,
        state=todo.state,
        user_id=user.id,
    )
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)

    return db_todo
```

---

## Testes

```python
def test_create_todo(client, token):
    response = client.post(
        '/todos/',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'title': 'Test todo',
            'description': 'Test todo description',
            'state': 'draft',
        },
    )
    assert response.json() == {
        'id': 1,
        'title': 'Test todo',
        'description': 'Test todo description',
        'state': 'draft',
    }
```

---

## Funciona?

> http://127.0.0.1:8000/docs

---

## Nem tudo são flores

```text
sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such table: todos
[SQL: INSERT INTO todos (title, description, state, user_id) VALUES (?, ?, ?, ?)]
[parameters: ('string', 'string', 'draft', 8)]
(Background on this error at: https://sqlalche.me/e/20/e3q8)
```

---

## Executando a migração

```bash
alembic revision --autogenerate -m "create todos table"
alembic upgrade head
```

--- 

## Funciona?

> http://127.0.0.1:8000/docs

---

# Relacionando tabelas

> TODO: Será que precisamos????

---

## Endpoint de GET

```python
from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from fast_zero.schemas import TodoList, TodoPublic, TodoSchema
# ...
@router.get('/', response_model=TodoList)
def list_todos(
    session: Session,
    user: CurrentUser,
    title: str = Query(None),
    description: str = Query(None),
    state: str = Query(None),
    offset: int = Query(None),
    limit: int = Query(None),
): ...
```

---

TODO:

- adicionar o código do get
- Fazer testes exaustivos no get
- patch e teste
- delete e teste
- quiz
- commit

---

# Exercícios

1. Adicione os campos `created_at` e `updated_at` na tabela `Todo`
   - Eles devem ser `init=False`
   - Deve usar `func.now()` para criação
   - O campo `updated_at` deve ter `onupdate`

2. Criar uma migração para que os novos campos sejam versionados e também aplicar a migração
3. Adicionar os campos `created_at` e `updated_at` no schema de saída dos endpoints. Para que esse valores sejam retornados na API.

---

# Quiz

Não esqueça de responder ao [quiz](https://fastapidozero.dunossauro.com/quizes/aula_09/) dessa aula

---

# Commit

```bash
git add .
git commit -m "Implementado os endpoints de tarefas"
```


<!-- mermaid.js -->
<script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"></script>
<script>mermaid.initialize({startOnLoad:true,theme:'dark'});</script>
<script src=" https://cdn.jsdelivr.net/npm/open-dyslexic@1.0.3/index.min.js "></script>
<link href=" https://cdn.jsdelivr.net/npm/open-dyslexic@1.0.3/open-dyslexic-regular.min.css " rel="stylesheet">
