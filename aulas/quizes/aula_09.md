# 09 - Criando Rotas CRUD para Gerenciamento de Tarefas em FastAPI

<?quiz?>
question: 01 - Qual o papel da classe 'TodoState' em nosso código?
answer: Fornece métodos para gerar IDs sequenciais para tarefas.
answer: Armazena o histórico de alterações das tarefas ao longo do tempo.
answer: Permite a criação de tarefas com diferentes níveis de prioridade.
answer-correct: Tipo com valores nomeados e constantes para representar estados de tarefas.
content:
  A classe `TodoState` define estados de tarefas (rascunho, pendente, etc.) com nomes claros, facilitando o código e garantindo segurança e agilidade na manutenção.
<?/quiz?>


<?quiz?>
question: 02 - Qual o significado da relação `user: Mapped[User] = relationship(...)` em nosso modelo?
answer: Define conexão entre usuários e tarefas (N:N) com lista inicializada e acesso bidirecional.
answer-correct: Estabelece relação entre usuários e tarefas (1:N) com lista não inicializada e acesso bidirecional.
answer: Cria vínculo entre usuários e tarefas (1:1) com lista não inicializada e acesso unidirecional.
answer: Estabelece relação entre usuários e tarefas (1:N) com lista inicializada e acesso unidirecional.
content:
  A relação `user: Mapped[User] = relationship(...)` define uma conexão 1:N entre usuários e tarefas, permitindo que um usuário tenha várias tarefas e cada tarefa esteja ligada a um único usuário. A lista de tarefas não é inicializada automaticamente e as entidades podem se acessar mutuamente.
<?/quiz?>


<?quiz?>
question: 03 - Qual o significado do parâmetro de consulta `state: str | None = None` no endpoint de busca?
answer: Permite filtrar resultados por valor de string obrigatório ('state'), não aceitando None.
answer: Filtra resultados por estado ('state'), com valor padrão 'pendente' se não especificado.
answer-correct: Habilita filtro por 'state' (string ou None), com valor padrão None se não especificado.
answer: Cria um parâmetro opcional 'state' que recebe floats para filtrar resultados.
content:
  O parâmetro `state: str | None = None` no FastAPI permite filtrar resultados por um valor de string opcional ('state'), que pode ser None por padrão.
<?/quiz?>

<?quiz?>
question: 04 - Qual a função do `FuzzyChoice` no Factory Boy?
answer-correct: Gera dados de teste aleatórios e realistas, facilitando a criação de testes de unidade robustos.
answer: Gera valores aleatórios para cada atributo de um objeto de teste, facilitando a criação de testes.
answer: Cria objetos de teste com valores predefinidos a partir de um conjunto de opções.
answer: Permite a geração de dados de teste aleatórios e realistas para diferentes tipos de dados.
content:
  O `FuzzyChoice` do Factory Boy gera valores aleatórios a partir de um conjunto predefinido, criando objetos de teste com dados realistas e facilitando testes de unidade robustos.
<?/quiz?>


<?quiz?>
question: 05 - Por qual razão usamos `# noqa` no endpoint `list_todos`:
answer: Para dizer aos QAs que esse código não é pra eles.
answer: Para dizer que esse código não será coberto por testes.
answer-correct: Para remover a checagem no linter na expressão.
content:
<?/quiz?>

<?quiz?>
question: 06 - Qual a função do `session.bulk_save_objects` nos testes de todo?
answer-correct: Inserir uma lista de objetos na session
answer: Salvar diversos objetos de uma vez no banco de dados
content:
<?/quiz?>

```quiz
{
    "questao": '07 - Qual a função do `exclude_unset=True` no código abaixo?',
	"opcoes": {
		"a": "Exclui os valores que não fazem parte do schema",
		"b": "Exclui os valores que não foram passados para o schema",
		"c": "Exclui os valores que são None no schema",
	},
	"correta": "c",
	"code" : """
```python hl_lines="6"
@router.patch('/{todo_id}', response_model=TodoPublic)
def patch_todo(
    todo_id: int, session: Session, user: CurrentUser, todo: TodoUpdate
):
    # ...
    for key, value in todo.model_dump(exclude_unset=True).items():
        setattr(db_todo, key, value)
```"""
}
```
