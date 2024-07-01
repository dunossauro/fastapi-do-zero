# 06 - Autenticação e Autorização com JWT

<?quiz?>
question: 01 - Qual a função da 'pwdlib' em nosso projeto?
answer-correct: Criar um hash da senha
answer-correct: Verificar se o texto limpo bate com o texto sujo
answer: Salvar as senhas em texto limpo
answer: Fazer validação das senhas
content:
<?/quiz?>

```quiz
{
    "questao": '02 - Qual a necessidade de adicionar a linha em destaque no endpoint de PUT?',
	"opcoes": {
		"a": "Validar a senha no momento do update",
		"b": "Criar o hash da senha durante a atualização",
		"c": "Pegar a senha antiga durante o update",
		"d": "Salvar a senha de forma limpa no banco de dados",
	},
	"correta": "b",
	"code" : """
```python hl_lines="4"
@app.put('/users/{user_id}', response_model=UserPublic)
# ...
    db_user.username = user.username
    db_user.password = get_password_hash(user.password)
    db_user.email = user.email
```"""
}
```

<?quiz?>
question: 03 - Qual o propósito da autenticação?
answer: Fornecer um mecanismo de tokens
answer-correct: Validar que o cliente é quem diz ser
answer: Garantir que só pessoas autorizadas possam executar ações
content:
<?/quiz?>

<?quiz?>
question: 04 - Qual a função do endpoint '/token'?
answer: Gerenciar a autorização do cliente
answer-correct: Fazer a autenticação do cliente
answer-correct: Renovar o token JWT
answer: Todas as respostas estão corretas
content:
<?/quiz?>

<?quiz?>
question: 05 - O 'OAuth2PasswordRequestForm' fornece:
answer: Um formulário de cadastro
answer-correct: Um formulário de autenticação
answer: Um formulário de autorização
answer: Um formulário de alteração de registro
content:
<?/quiz?>

<?quiz?>
question: 06 - Qual a função do token JWT?
answer: Fornecer informações sobre o cliente para o servidor
answer: Gerenciar o tempo de validade do token
answer: Carregar dados sobre autorização
answer-correct: Todas as respostas estão corretas
content:
<?/quiz?>

<?quiz?>
question: 07 - Qual o objetivo da claim 'sub'?
answer: Guardar o tempo de validade do token
answer: Identificar o servidor que gerou o token
answer-correct: Identificar qual cliente gerou o token
answer: Identificar o email do cliente
content:
<?/quiz?>

<?quiz?>
question: 08 - Qual a função da 'secret_key'?
answer: Usar como base para criptografar a senha do cliente com Argon2
answer: Usar como base para geração do HTTPS
answer-correct: Ussar como base para assinar o Token com HS256
content:
<?/quiz?>

<?quiz?>
question: 09 - Qual o objetivo da função 'current_user'?
answer: Gerenciar a autenticação dos clientes
answer: Validar o token JWT
answer-correct: Gerenciar a autorização dos endpoints
answer: Saber que é o usuário logado
content:
<?/quiz?>
