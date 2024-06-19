# 03 - Estruturando o Projeto e Criando Rotas CRUD

<?quiz?>
question: 01 - O método POST pode ser associado a qual letra da sigla CRUD?
answer: U
answer: D
answer-correct: C
answer: R
content:
<?/quiz?>

<?quiz?>
question: 02 - Quando um recurso é criado via POST, qual o Status deve ser retornado para sucesso?
answer: 200
answer-correct: 201
answer: 202
answer: 301
content:
<?/quiz?>


<?quiz?>
question: 03 - Quando um schema não é respeitado pelo cliente, qual o status retornado?
answer: 500
answer: 404
answer: 401
answer-correct: 422
content:
<?/quiz?>

<?quiz?>
question: 04 - O FastAPI retorna qual status para quando o servidor não respeita o contrato? 
answer: UNPROCESSABLE ENTITY
answer: I'M A TEAPOT
answer-correct: INTERNAL SERVER ERROR
answer: NOT IMPLEMENTED
content:
<?/quiz?>

```quiz
{
    "questao": "05 - O que faz a seguinte fixture",
	"opcoes": {
		"a": "Faz uma requisição a aplicação",
		"b": "Cria um cliente de teste reutilizável",
		"c": "Faz o teste automaticamente",
	},
	"correta": "b",
	"code" : """
```python
@pytest.fixture()
def client():
    return TestClient(app)
```"""
}
```


<?quiz?>
question: 06 - Qual código de resposta deve ser enviado quando o recurso requerido não for encontrado?
answer: 201
answer-correct: 404
answer: 401
answer: 500
content:
<?/quiz?>

```quiz
{
    "questao": "07 - Sobre o relacionamento dos schemas, qual seria a resposta esperada pelo cliente em UserList?",
	"opcoes": {
		"a": '{"username": "string", "email": "e@mail.com"}',
		"b": '[{"username": "string", "email": "e@mail.com"}]',
		"c": "As duas estão corretas",
	},
	"correta": "b",
	"code" : """
```python
class UserPublic(BaseModel):
    username: str
    email: str


class UserList(BaseModel):
    users: list[UserPublic]
```"""
}
```

{% include "templates/mais_quiz.md" %}
