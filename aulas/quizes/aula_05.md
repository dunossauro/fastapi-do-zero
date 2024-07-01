# 05 - Integrando Banco de Dados a API

```quiz
{
    "questao": '01 - Qual a função de adicionarmos a função "Depends" no seguinte código:',
	"opcoes": {
		"a": "Indicar que a função depende de algo",
		"b": "Documentar no schema os dados que são requeridos para chamar o endpoint",
		"c": "Executar a função 'get_session' e passar seu resultado para função",
		"d": "Indicar que a função 'get_session' tem que ser executada antes da 'create_user'",
	},
	"correta": "c",
	"code" : """
```python
@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(
    user: UserSchema,
	session: Session = Depends(get_session)
):
```"""
}
```

```quiz
{
    "questao": '02 - Sobre a injeção na fixture podemos afirmar que:',
	"opcoes": {
		"a": "Ela removerá dependência do código durante a execução do teste",
		"b": "Será feita a sobreescrita de uma dependencia por outra durante o teste",
		"c": "A dependência 'get_session' será forçada durante o teste",
	},
	"correta": "b",
	"code" : """
```python
with TestClient(app) as client:
    app.dependency_overrides[get_session] = get_session_override
	yield client

app.dependency_overrides.clear()
```"""
}
```

```quiz
{
    "questao": '03 - Essa fixture no banco de dados garante que:',
	"opcoes": {
		"a": "O banco de dados estará em memória",
		"b": "Não será executada a verificação entre a thread do banco e do teste",
		"c": "Será usado um pool de tamanho fixo",
		"d": "Criará uma conexão com o banco de dados para usar nos testes",
		"e": "todas as alternativas anteriores",
	},
	"correta": "e",
	"code" : """
```python
@pytest.fixture()
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
```"""
}
```

```quiz
{
    "questao": '04 - Para que o cliente requisite o campo "limit" ele deve usar a url:',
	"opcoes": {
		"a": "/users/?limit=10",
		"b": "/users/limit/10",
		"c": "/users/limit=10?",
		"d": "/users/&limit=10",
	},
	"correta": "a",
	"code" : """
```python
@app.get('/users/', response_model=UserList)
def read_users(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
```"""
}
```

<?quiz?>
question: 05 - Quais os padrões de projeto implementados pela Session?
answer-correct: Repositório
answer-correct: Unidade de trabalho
answer: Composite
answer: Proxy
content:
<?/quiz?>

<?quiz?>
question: 06 - O que faz o método session.commit()?
answer: Faz um commit no git
answer: Persiste os dados no banco de dados
answer-correct: Executa as transações na sessão
answer: Abre uma conexão com o banco de dados
content:
<?/quiz?>

<?quiz?>
question: 07 - O que faz o método session.refresh(obj)?
answer: Atualiza a conexão com o banco de dados
answer: Atualiza dos dados da sessão
answer-correct: Sincroniza o objeto do ORM com o banco de dados
answer: Sincroniza a sessão com o banco de dados
content:
<?/quiz?>

```quiz
{
    "questao": '08 - O que o "|" siginifica na query?',
	"opcoes": {
		"a": "user.username 'E' user.email",
		"b": "user.username 'SEM' user.email",
		"c": "user.username 'OU' user.email",
		"d": "user.username 'COM' user.email",
	},
	"correta": "c",
	"code" : """
```python hl_lines="3"
session.scalar(
    select(User).where(
        (User.username == user.username) | (User.email == user.email)
    )
)
```"""
}
```

<?quiz?>
question: 09 - Quando usamos o método 'model_validate' de um schema do Pydantic estamos:
answer: Validando um JSON com o modelo
answer: Validando um request com o modelo
answer-correct: Converte um objeto em um schema
answer: Coverte um objeto em JSON
content:
<?/quiz?>

<?quiz?>
question: 10 - Quando usamos 'model_config' em um schema do Pydantic estamos:
answer-correct: Alterando o comportamento de 'model_validade'
answer: Adicionando mais um campo de validação
answer: Alterando a estrutura do modelo
content:
<?/quiz?>
