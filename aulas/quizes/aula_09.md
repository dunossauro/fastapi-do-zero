# 09 - Criando Rotas CRUD para Gerenciamento de Tarefas em FastAPI

<?quiz?>
question: 01 - Qual o papel da classe 'TodoState' em nosso código Python?
answer: Fornece métodos para gerar IDs sequenciais para tarefas.
answer: Armazena o histórico de alterações das tarefas ao longo do tempo.
answer: Permite a criação de tarefas com diferentes níveis de prioridade.
answer-correct: Tipo com valores nomeados e constantes para representar estados de tarefas.
content:
  A classe `TodoState` define estados de tarefas (rascunho, pendente, etc.) com nomes claros, facilitando o código e garantindo segurança e agilidade na manutenção.
<?/quiz?>


<?quiz?>
question: 02 - Qual o significado da relação `user: Mapped[User] = relationship(...)` no código Python fornecido?
answer: Define conexão entre usuários e tarefas (N:N) com lista inicializada e acesso bidirecional.
answer: Cria vínculo entre usuários e tarefas (1:1) com lista não inicializada e acesso unidirecional.
answer: Estabelece relação entre usuários e tarefas (1:N) com lista inicializada e acesso unidirecional.
answer-correct: Estabelece relação entre usuários e tarefas (1:N) com lista não inicializada e acesso bidirecional.
content:
  A relação `user: Mapped[User] = relationship(...)` define uma conexão 1:N entre usuários e tarefas, permitindo que um usuário tenha várias tarefas e cada tarefa esteja ligada a um único usuário. A lista de tarefas não é inicializada automaticamente e as entidades podem se acessar mutuamente.
<?/quiz?>


<?quiz?>
question: 03 - Qual o significado do parâmetro de consulta `state: str | None = None` no FastAPI?
answer: Permite filtrar resultados por valor de string obrigatório ('state'), não aceitando None.
answer: Filtra resultados por estado ('state'), com valor padrão 'pendente' se não especificado.
answer: Cria um parâmetro opcional 'state' que recebe floats para filtrar resultados.
answer-correct: Habilita filtro por 'state' (string ou None), com valor padrão None se não especificado.
content:
  O parâmetro `state: str | None = None` no FastAPI permite filtrar resultados por um valor de string opcional ('state'), que pode ser None por padrão.
<?/quiz?>

<?quiz?>
question: 04 - Qual a função do `FuzzyChoice` no Factory Boy?
answer: Gera valores aleatórios para cada atributo de um objeto de teste, facilitando a criação de testes.
answer: Cria objetos de teste com valores predefinidos a partir de um conjunto de opções.
answer: Permite a geração de dados de teste aleatórios e realistas para diferentes tipos de dados.
answer-correct: Gera dados de teste aleatórios e realistas, facilitando a criação de testes de unidade robustos.
content:
  O `FuzzyChoice` do Factory Boy gera valores aleatórios a partir de um conjunto predefinido, criando objetos de teste com dados realistas e facilitando testes de unidade robustos.
<?/quiz?>


{% include "templates/mais_quiz.md" %}
