# 01 - Configurando o Ambiente de Desenvolvimento

<?quiz?>
question: 01 - Qual a função do pipx?
answer: Criar e gerenciar ambientes virtuais para bibliotecas
answer-correct: Instalar bibliotecas isoladamente de forma global
answer: Uma alternativa ao pip
answer: Uma alternativa ao venv
content:
<?/quiz?>

<?quiz?>
question: 02 - Qual a função do Poetry?
answer: Uma alternativa ao pip
answer-correct: Gerenciar um projeto python
answer: Tem o mesmo propósito do pipx
content:
<?/quiz?>

<?quiz?>
question: 03 - O que faz o comando "fastapi dev"?
answer: Cria um ambiente de desenvolvimento para o FastAPI
answer: Inicia o servidor de produção do FastAPI
answer-correct: Inicia o Uvicorn em modo de desenvolvimento
answer: Instala o FastAPI
content:
<?/quiz?>

<?quiz?>
question: 04 - Ao que se refere o endereço "127.0.0.1"?
answer-correct: Ao endereço de rede local
answer-correct: Caminho de loopback
answer: Endereço do FastAPI
content:
<?/quiz?>

<?quiz?>
question: 05 - A flag do poetry "--group dev" instala os pacotes
answer: de produção
answer-correct: de desenvolvimento
answer: de testes
content:
<?/quiz?>

<?quiz?>
question: 06 - Qual a função do taskipy?
answer-correct: Criar "atalhos" para comandos mais simples
answer-correct: Facilitar o manuseio das operações de terminal
answer: Instalar ferramentas de desenvolvimento
answer: Gerenciar o ambiente virtual
content:
<?/quiz?>

<?quiz?>
question: 07 - O pytest é:
answer: um linter
answer: um formatador de código
answer-correct: framework de testes
content:
<?/quiz?>

<?quiz?>
question: 08 - Qual a ordem esperada de execução de um teste?
answer-correct: arrange, act, assert
answer: act, assert, arrange
answer: arrange, assert, act
content:
<?/quiz?>

```quiz
{
    "questao": "09 - Dentro do nosso teste, qual a função da chamada na linha em destaque?",
	"opcoes": {
		"a": "assert",
		"b": "arrange",
		"c": "act",
	},
	"correta": "c",
	"code" : """
```python hl_lines="4"
def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}
```"""
}
```

<?quiz?>
question: 10 - Na cobertura de testes, o que quer dizer "Stmts"?
answer: Linha cobertas pelo teste
answer: Linhas não cobertas pelo teste
answer-correct: Linhas de código
content:
<?/quiz?>
