# 05 - Integrando Banco de Dados a API

<quiz>
Qual a função de adicionarmos a função `Depends` no seguinte código:

```python
@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(
    user: UserSchema,
	session: Session = Depends(get_session)
):
```

- [ ] Indicar que a função depende de algo
- [ ] Documentar no schema os dados que são requeridos para chamar o endpoint
- [x] Executar a função `get_session` e passar seu resultado para função
- [ ] Indicar que a função `get_session` tem que ser executada antes da `create_user`
</quiz>

<quiz>
Sobre a injeção na fixture podemos afirmar que:

```python
with TestClient(app) as client:
    app.dependency_overrides[get_session] = get_session_override
	yield client

app.dependency_overrides.clear()
```

- [ ] Ela removerá dependência do código durante a execução do teste
- [x] Será feita a sobreescrita de uma dependencia por outra durante o teste
- [ ] A dependência `get_session` será forçada durante o teste
</quiz>

<quiz>
Essa fixture no banco de dados garante que:

```python
@pytest.fixture
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
```

- [ ] O banco de dados estará em memória
- [ ] Não será executada a verificação entre a thread do banco e do teste
- [ ] Será usado um pool de tamanho fixo
- [ ] Criará uma conexão com o banco de dados para usar nos testes
- [x] Todas as alternativas anteriores
</quiz>

<quiz>
Para que o cliente requisite o campo `limit` ele deve usar a url:

```python
@app.get('/users/', response_model=UserList)
def read_users(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
```

- [x] `/users/?limit=10`
- [ ] `/users/limit/10`
- [ ] `/users/limit=10?`
- [ ] `/users/&limit=10`
</quiz>


<quiz>
Quais os padrões de projeto implementados pela `Session`?
- [x] Repositório
- [x] Unidade de trabalho
- [ ] Composite
- [ ] Proxy
</quiz>

<quiz>
O que faz o método `session.commit()`?
- [ ] Faz um commit no git
- [ ] Persiste os dados no banco de dados
- [x] Executa as transações na sessão
- [ ] Abre uma conexão com o banco de dados
</quiz>

<quiz>
O que faz o método `session.refresh(obj)`?
- [ ] Atualiza a conexão com o banco de dados
- [ ] Atualiza dos dados da sessão
- [x] Sincroniza o objeto do ORM com o banco de dados
- [ ] Sincroniza a sessão com o banco de dados
</quiz>

<quiz>
O que o `|` siginifica na query?

```python hl_lines="3"
session.scalar(
    select(User).where(
        (User.username == user.username) | (User.email == user.email)
    )
)
```

- [ ] `user.username` E `user.email`
- [ ] `user.username` SEM `user.email`
- [x] `user.username` OU `user.email`
- [ ] `user.username` COM `user.email`
</quiz>

<quiz>
Quando usamos o método `model_validate` de um schema do Pydantic estamos:
- [ ] Validando um JSON com o modelo
- [ ] Validando um request com o modelo
- [x] Converte um objeto em um schema
- [ ] Coverte um objeto em JSON
</quiz>

<quiz>
Quando usamos `model_config` em um schema do Pydantic estamos:
- [x] Alterando o comportamento de 'model_validate'
- [ ] Adicionando mais um campo de validação
- [ ] Alterando a estrutura do modelo
</quiz>
