# 07 - Refatorando a Estrutura do Projeto

<?quiz?>
question: 01 - Quais são as funções do "Router" do FastAPI
answer-correct: Criar uma "sub-aplicação"
answer-correct: Isolar endpoints por domínio
answer-correct: Facilitar a manutenção do código
answer: Melhorando o desempenho da aplicação
content:
<?/quiz?>

<?quiz?>
question: 02 - Sobre o parâmetro "prefix" do router, podemos afirmar que:
answer: Adicionar os endpoints no roteador
answer: Fazer as chamadas unificadas do enpoint 
answer-correct: Padronizar um prefixo para N endpoints
content:
<?/quiz?>

<?quiz?>
question: 03 - Qual a função do parâmetro 'tag' nos routers?
answer: Dizer quais parâmetros devem ser passados ao endpoints
answer: Colocar um prefixo nos endpoints
answer-correct: Agrupar os endpoins do mesmo domínio na documentação
answer: Adicionar cores diferentes no swagger
content:
<?/quiz?>

<?quiz?>
question: 04 - Qual a função do tipo "Annotated" no FastAPI!
answer: Reduzir o tamanho das funções
answer: Reutilizar anotações em N endpoints
answer: Atribuir metadados aos tipos
answer-correct: Todas as alternativas
content:
<?/quiz?>

```quiz
{
    "questao": '05 - O que o "Annotated" faz nesse código?',
	"opcoes": {
		"a": "Diz que o parâmetro 'session' é do tipo 'Session' e depende de 'get_session'",
		"b": "Diz que o parâmetro 'session' é do tipo 'Annotated'",
		"c": "Faz a troca de 'session' por 'Session'",
	},
	"correta": "a",
	"code" : """
```python hl_lines="4"
@app.put('/users/{user_id}', response_model=UserPublic)
def endpoint(session: Annotated[Session, Depends(get_session)])
```"""
}
```
