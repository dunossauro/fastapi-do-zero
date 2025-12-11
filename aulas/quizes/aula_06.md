# 06 - Autenticação e Autorização com JWT

<quiz>
Qual a função da `pwdlib` em nosso projeto?
- [x] Criar um hash da senha
- [x] Verificar se o texto limpo bate com o texto sujo
- [ ] Salvar as senhas em texto limpo
- [ ] Fazer validação das senhas
</quiz>

<quiz>
Qual a necessidade de adicionar a linha em destaque no endpoint de PUT?

```python hl_lines="4"
@app.put('/users/{user_id}', response_model=UserPublic)
# ...
    db_user.username = user.username
    db_user.password = get_password_hash(user.password)
    db_user.email = user.email
```

- [ ] Validar a senha no momento do update
- [x] Criar o hash da senha durante a atualização
- [ ] Pegar a senha antiga durante o update
- [ ] Salvar a senha de forma limpa no banco de dados
</quiz>


<quiz>
Qual o propósito da autenticação?
- [ ] Fornecer um mecanismo de tokens
- [x] Validar que o cliente é quem diz ser
- [ ] Garantir que só pessoas autorizadas possam executar ações
</quiz>

<quiz>
Qual a função do endpoint `/token`?
- [ ] Gerenciar a autorização do cliente
- [x] Fazer a autenticação do cliente
- [x] Renovar o token JWT
- [ ] Todas as respostas estão corretas
</quiz>

<quiz>
O `OAuth2PasswordRequestForm` fornece:
- [ ] Um formulário de cadastro
- [x] Um formulário de autenticação
- [ ] Um formulário de autorização
- [ ] Um formulário de alteração de registro
</quiz>

<quiz>
Qual a função do token JWT?
- [ ] Fornecer informações sobre o cliente para o servidor
- [ ] Gerenciar o tempo de validade do token
- [ ] Carregar dados sobre autorização
- [x] Todas as respostas estão corretas
</quiz>

<quiz>
Qual o objetivo da claim `sub`?
- [ ] Guardar o tempo de validade do token
- [ ] Identificar o servidor que gerou o token
- [x] Identificar qual cliente gerou o token
- [ ] Identificar o email do cliente
</quiz>

<quiz>
Qual a função da `secret_key`?
- [ ] Usar como base para criptografar a senha do cliente com Argon2
- [ ] Usar como base para geração do HTTPS
- [x] Usar como base para assinar o Token com HS256
</quiz>

<quiz>
Qual o objetivo da função `get_current_user`?
- [ ] Gerenciar a autenticação dos clientes
- [ ] Validar o token JWT
- [x] Gerenciar a autorização dos endpoints
- [ ] Saber que é o usuário logado
</quiz>


<quiz>
Qual o objetivo da claim `exp`?
- [ ] Dizer se o token está autorizado
- [ ] Especificar o nome do usuário
- [ ] Definir o tempo de criação do token
- [x] Transmitir o tempo de expiração do token
</quiz>
