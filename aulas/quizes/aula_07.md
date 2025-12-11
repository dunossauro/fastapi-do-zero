# 07 - Refatorando a Estrutura do Projeto

<quiz>
Quais são as funções do `Router` do FastAPI
- [x] Criar uma "sub-aplicação"
- [x] Isolar endpoints por domínio
- [x] Facilitar a manutenção do código
- [ ] Melhorando o desempenho da aplicação
</quiz>

<quiz>
Sobre o parâmetro `prefix` do router, podemos afirmar que:
- [ ] Adicionar os endpoints no roteador
- [ ] Fazer as chamadas unificadas do enpoint
- [x] Padronizar um prefixo para N endpoints
</quiz>

<quiz>
Qual a função do parâmetro `tag` nos routers?
- [ ] Dizer quais parâmetros devem ser passados ao endpoints
- [ ] Colocar um prefixo nos endpoints
- [x] Agrupar os endpoins do mesmo domínio na documentação
- [ ] Adicionar cores diferentes no swagger
</quiz>

<quiz>
Qual a função do tipo `Annotated` no FastAPI!
- [ ] Reduzir o tamanho das funções
- [ ] Reutilizar anotações em N endpoints
- [ ] Atribuir metadados aos tipos
- [x] Todas as alternativas
</quiz>

<quiz>
O que o `Annotated` faz nesse código?

```python hl_lines="2"
@app.put('/users/{user_id}', response_model=UserPublic)
def endpoint(session: Annotated[Session, Depends(get_session)])
```

- [x] Diz que o parâmetro `session` é do tipo `Session` e depende de `get_session`
- [ ] Diz que o parâmetro `session` é do tipo `Annotated`
- [ ] Faz a troca de `session` por `Session`
</quiz>

<quiz>
O que o `include_router` faz nesse código?

```python
app = FastAPI()

app.include_router(users.router)
```

- [x] Adiciona as rotas definidas do router `users`
- [ ] Cria um novo app fastAPI para o router
- [ ] Substitui as rotas existentes pelas rotas de `users`
- [ ] Exclui as rotas de `users` da aplicação
</quiz>


<quiz>
O que faz `Annotated[FilterPage, Query()]` no nosso endpoint?
- [x] Ignora parâmetros passados que não estejam em `FilterPage`
- [x] Adiciona os campos de `FilterPage` na documentação
- [x] Valida os tipos e valores passados via querystring
- [x] Transforma os parâmetros de `FilterPage` em querystring
</quiz>

<quiz>
Qual o impacto das constantes movidas para a classe `Settings`?
- [ ] Excluir a necessidade um arquivo .env
- [x] Pode alterar configurações sem alterar o código fonte
- [ ] Poder alterar os valores das contantes em tempo de execução
- [ ] Simplificar as chamadas de código
</quiz>

<quiz>
Por qual motivo dividimos a aplicação em routers?
- [ ] Melhorar o desempenho da aplicação
- [x] Melhorar a organização do código
- [x] Facilitar a manutenção
- [ ] Todas as alternativas estão corretas
</quiz>

<quiz>
Por qual motivo `read_root` não foi migrado para nenhum router?
- [ ] É só um exemplo de código
- [ ] Por que ela retorna HTML
- [x] Não pertence a nenhum domínio dos routers em específico
- [ ] Por que não faz uso de Session
</quiz>
