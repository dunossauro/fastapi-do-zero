# 08 - Tornando o sistema de autenticação robusto

```quiz
{
    "questao": '01 - Sobre o Factory-boy. O que siginifica a classe Meta?',
	"opcoes": {
		"a": "Diz que será usada uma metaclasse",
		"b": "Explica ao Factory qual objeto ele deve se basear",
		"c": "Extente a classe Factory com os parâmetros de Meta",
	},
	"correta": "b",
	"code" : """
```python hl_lines="4"
class UserFactory(factory.Factory):
    class Meta:
        model = User
```"""
}
```

<?quiz?>
question: 02 - Ainda sobre o Factory-boy. O que siginifica "factory.Sequence"?
answer: Criará uma sequência de Metas
answer-correct: Adicionará +1 em cada objeto criado
answer: Monta uma sequência de objetos
answer: Cria um novo objeto do factory
content:
<?/quiz?>


<?quiz?>
question: 03 - Ainda sobre o Factory-boy. O que siginifica "factory.LazyAttribute"?
answer-correct: Diz que o atributo será criado em tempo de execução
answer-correct: Diz que o atributo usará outros atributos para ser inicializado
answer-correct: Usa outros campos para ser composto
answer: Cria um atributo independênte
content:
<?/quiz?>

```quiz
{
    "questao": '04 - O que faz o gerenciador de contexto "freeze_time"?',
	"opcoes": {
		"a": "Pausa o tempo nas instruções dentro do 'with'",
		"b": "Congela o tempo da função toda",
		"c": "Muda a hora do computador para um bloco",
	},
	"correta": "a",
	"code" : """
```python hl_lines="1"
with freeze_time('2023-07-14 12:00:00'):
    response = client.post(
        '/auth/token',
        data={'username': user.email, 'password': user.clean_password},
    )
```"""
}
```

<?quiz?>
question: 05 - O que levanta o erro "ExpiredSignatureError"?
answer: Quando deu erro no valor de 'exp'
answer: Quando não deu certo avaliar a claim de 'exp'
answer-correct: Quando a claim de 'exp' tem um tempo expirado
content:
<?/quiz?>
