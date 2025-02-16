# 08 - Tornando o projeto assíncrono

<?quiz?>
question: 01 - Escalonamento no asyncio é a capacidade do código de:
answer: Executar tarefas simultaneamente
answer: Alternar entre a execução de funções
answer: Fazer com que o código seja bloqueante
answer-correct: Alternar entre a execução de corrotinas
content:
<?/quiz?>


<?quiz?>
question: 02 - Dizemos que um código é cooperativo quando:
answer-correct: Quando ele cede a vez para outro código ser executado
answer-correct: Quando ele usa a palavra reservada await
answer-correct: Quando ele permite ser escalonado
answer: Quando ele usa async def
content:
<?/quiz?>


```quiz
{
    "questao": '03 - Sobre o uso de await no código, podemos afirmar que:',
	"opcoes": {
		"a": "Permite escalonamento durante a comunicação com o banco de dados",
		"b": "Bloqueia a execução até que o commit seja concluído",
		"c": "Cria uma nova corrotina",
		"d": "Faz cooperação com o banco de dados",
	},
	"correta": "a",
	"code" : """
```python hl_lines="8"
@pytest.mark.asyncio 
async def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username='alice', password='secret', email='teste@test'
        )
        session.add(new_user)
        await session.commit() 
```"""
}
```

<?quiz?>
question: 04 - Qual a função do loop de eventos?
answer-correct: Gerenciar a execução de corrotinas de maneira ordenada
answer: Executar corrotinas simultaneamente
answer-correct: Escalonar entre código cooperativo
answer-correct: Tornar a execução não bloqueante
content:
<?/quiz?>


```quiz
{
    "questao": '05 - Qual a necessidade de usarmos "asyncio.run"?',
	"opcoes": {
		"a": "Executar tarefas não bloqueantes de forma não bloqueante",
		"b": "Bloquear o código durante execuções não bloqueantes",
		"c": "Tonar a execução de funções síncronas em assíncronas",
	},
	"correta": "c",
	"code" : """
```python
run(corrotina())
```"""
}
```

<?quiz?>
question: 06 - Qual a função do greenlet no projeto?
answer-correct: Permitir que o SQLAlchemy faça programação assíncrona
answer: Permitir que o coverage cubra funções async
answer: Substituir o asyncio
answer: Criar loops de eventos
content:
<?/quiz?>


<?quiz?>
question: 07 - Qual a função da flag "-k" no pytest?
answer-correct: Executar todos os testes com nomes correspondentes a flag
answer: Listar todos os testes que podem ser executados
answer: Matar (kill) todos os testes que não funcionarem
answer: Pausar a execução dos testes caso um falhe
content:
<?/quiz?>


```quiz
{
    "questao": '08 - Qual a função de "pytest_asyncio.fixture" no código?',
	"opcoes": {
		"a": "Cria uma fixture bloqueante",
		"b": "Cria uma fixture que só pode ser usada em testes assíncronos",
		"c": "Cria uma fixture executada pelo loop de eventos",
	},
	"correta": "c",
	"code" : """
```python
@pytest_asyncio.fixture
async def session():
    # ...
```"""
}
```


```quiz
{
    "questao": '09 - Ao que se refere "expire_on_commit=False" na criação da sessão?',
	"opcoes": {
		"a": "Expira os dados não commitados",
		"b": "Não limpa a sessão após o commit",
		"c": "Cria uma sessão com tempo de vida",
	},
	"correta": "b",
	"code" : """
```python
async def get_session():
    async with AsyncSession(engine, expire_on_commit=False) as session: 
        yield session
```"""
}
```


<?quiz?>
question: 10 - Adicionar "async def" ao código cria:
answer: Uma função assíncrona
answer-correct: Uma corrotina
answer: Um loop de eventos
answer: Um código bloqueante
content:
<?/quiz?>
