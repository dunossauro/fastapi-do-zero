# 10 - Criando Rotas CRUD para Gerenciamento de Tarefas em FastAPI

<quiz>
Qual o papel da classe `TodoState` em nosso código?
- [ ] Fornece métodos para gerar IDs sequenciais para tarefas.
- [ ] Armazena o histórico de alterações das tarefas ao longo do tempo.
- [ ] Permite a criação de tarefas com diferentes níveis de prioridade.
- [x] Tipo com valores nomeados e constantes para representar estados de tarefas.

A classe `TodoState` define estados de tarefas (rascunho, pendente, etc.) com nomes claros, facilitando o código e garantindo segurança e agilidade na manutenção.
</quiz>

<quiz>
Qual o significado da relação `user: Mapped[User] = relationship(...)` em nosso modelo?
- [ ] Define conexão entre usuários e tarefas (N:N) com lista inicializada e acesso bidirecional.
- [x] Estabelece relação entre usuários e tarefas (1:N) com lista não inicializada e acesso bidirecional.
- [ ] Cria vínculo entre usuários e tarefas (1:1) com lista não inicializada e acesso unidirecional.
- [ ] Estabelece relação entre usuários e tarefas (1:N) com lista inicializada e acesso unidirecional.

A relação `user: Mapped[User] = relationship(...)` define uma conexão 1:N entre usuários e tarefas, permitindo que um usuário tenha várias tarefas e cada tarefa esteja ligada a um único usuário. A lista de tarefas não é inicializada automaticamente e as entidades podem se acessar mutuamente.
</quiz>

<quiz>
Qual o significado do parâmetro de consulta `state: str | None = None` no endpoint de busca?
- [ ] Permite filtrar resultados por valor de string obrigatório ('state'), não aceitando None.
- [ ] Filtra resultados por estado ('state'), com valor padrão 'pendente' se não especificado.
- [x] Habilita filtro por 'state' (string ou None), com valor padrão None se não especificado.
- [ ] Cria um parâmetro opcional 'state' que recebe floats para filtrar resultados.

O parâmetro `state: str | None = None` no FastAPI permite filtrar resultados por um valor de string opcional ('state'), que pode ser None por padrão.
</quiz>

<quiz>
Qual a função do `FuzzyChoice` no Factory Boy?
- [ ] Gera valores aleatórios para cada atributo de um objeto de teste, facilitando a criação de testes.
- [ ] Cria objetos de teste com valores predefinidos a partir de um conjunto de opções.
- [x] Gera dados de teste aleatórios e realistas, facilitando a criação de testes de unidade robustos.
- [ ] Permite a geração de dados de teste aleatórios e realistas para diferentes tipos de dados.

O `FuzzyChoice` do Factory Boy gera valores aleatórios a partir de um conjunto predefinido, criando objetos de teste com dados realistas e facilitando testes de unidade robustos.
</quiz>

<quiz>
Qual a função da classe `Meta` no Factory Boy?
- [x] Definir um modelo base a ser usado no factory
- [ ] Definir o comportamento de como as instâncias de factory devem ser salvas no banco
- [ ] Controlar os valores padrão para os campos do modelo durante a criação dos objetos
- [ ] Criar instâncias de fábrica de forma anônima sem vincular a um modelo específico
</quiz>

<quiz>
Quando chamamos `TodoFactory.create_batch` o que estamos fazendo?
- [x] Criando N instâncias de Todo
- [ ] Modificando atributos específicos de uma instância de Todo
- [ ] Salvando as instâncias de Todo diretamente no banco de dados
- [ ] Criando uma única instância de Todo de forma assíncrona
</quiz>

<quiz>
Qual a função do `session.add_all` nos testes de todo?
- [ ] Salvar diversos objetos de uma vez no banco de dados
- [ ] Adicionar objetos diretamente à tabela do banco sem passar pela session
- [x] Inserir uma lista de objetos na session
- [ ] Atualizar objetos existentes na session
</quiz>

<quiz>
Qual a função do `exclude_unset=True` no código abaixo?

```python hl_lines="6"
@router.patch('/{todo_id}', response_model=TodoPublic)
def patch_todo(
    todo_id: int, session: Session, user: CurrentUser, todo: TodoUpdate
):
    # ...
    for key, value in todo.model_dump(exclude_unset=True).items():
        setattr(db_todo, key, value)
```

- [ ] Exclui os valores que não fazem parte do schema
- [ ] Exclui os valores que não foram passados para o schema
- [x] Exclui os valores que são `None` no schema
</quiz>

<quiz>
No schema `TodoUpdate` por que todos os valores são opcionais?

```python
class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    state: TodoState | None = None
```

- [ ] Porque todos os campos têm valores padrão definidos
- [ ] Porque a classe é derivada de uma classe base que permite campos opcionais
- [x] Porque os tipos dos campos permitem o valor None, tornando-os opcionais
- [ ] Porque a classe utiliza um modelo de validação assíncrona
</quiz>

<quiz>
O que a querystring `?title=Test` todo 1 quer dizer?

```python
response = client.get(
    '/todos/?title=Test todo 1',
    headers={'Authorization': f'Bearer {token}'},
)
```

- [ ] Que o título da todo será atualizado para 'Test todo 1'
- [ ] Que a busca retornará todos os itens com título que sejam iguais 'Test todo 1'
- [ ] Que a resposta será um erro, pois o parâmetro 'title' é obrigatório
- [x] Que a busca retornará todos os itens com título que contenham 'Test todo 1'
</quiz>
