# 03 - Estruturando o Projeto e Criando Rotas CRUD

<quiz>
O método POST pode ser associado a qual letra da sigla CRUD?
- [ ] U
- [ ] D
- [x] C
- [ ] R
</quiz>

<quiz>
Quando um recurso é criado via POST, qual o Status deve ser retornado para sucesso?
- [ ] 200
- [x] 201
- [ ] 202
- [ ] 301
</quiz>

<quiz>
Quando um schema não é respeitado pelo cliente, qual o status retornado?
- [ ] 500
- [ ] 404
- [ ] 401
- [x] 422
</quiz>

<quiz>
O FastAPI retorna qual status para quando o servidor não respeita o contrato?
- [ ] UNPROCESSABLE ENTITY
- [ ] I'M A TEAPOT
- [x] INTERNAL SERVER ERROR
- [ ] NOT IMPLEMENTED
</quiz>

<quiz>
O que faz a seguinte fixture?

```python
@pytest.fixture
def client():
    return TestClient(app)
```

- [ ] Faz uma requisição a aplicação
- [x] Cria um cliente de teste reutilizável
- [ ] Faz o teste automaticamente

</quiz>

<quiz>
Qual código de resposta deve ser enviado quando o recurso requerido não for encontrado?
- [ ] 201
- [x] 404
- [ ] 401
- [ ] 500
</quiz>

<quiz>
Sobre o relacionamento dos schemas, qual seria a resposta esperada pelo cliente em `UserList`?

```python
class UserPublic(BaseModel):
    username: str
    email: str


class UserList(BaseModel):
    users: list[UserPublic]
```

- [ ] `{"users": {"username": "string", "email": "e@mail.com"}}`
- [x] `{"users": [{"username": "string", "email": "e@mail.com"}]}`
- [ ] As duas estão corretas

</quiz>

<quiz>
`HTTPException` tem a função de:
- [ ] Criar um erro de servidor
- [x] Retornar um erro ao cliente
- [ ] Fazer uma validação HTTP
</quiz>

<quiz>
`users/{user_id}` permite:
- [x] Parametrizar a URL
- [x] Pedir por um recurso com id específico
- [x] Aumentar a flexibilidade dos endpoints
</quiz>

<quiz>
Qual a função desse bloco de código nos endpoints de PUT E DELETE?

```python
if user_id > len(database) or user_id < 1:
	raise HTTPException(
		status_code=HTTPStatus.NOT_FOUND, detail='User not found'
	)
```

- [x] Garantir que só sejam chamados id válidos
- [ ] Montar um novo schema do pydantic
- [ ] Dizer ao cliente que o schema dele tem um erro
- [ ] Criar um erro de servidor
</quiz>
