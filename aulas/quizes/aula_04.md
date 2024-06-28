# 04 - Configurando o Banco de Dados e Gerenciando Migrações com Alembic

<?quiz?>
question: 01 - Qual a função do sqlalchemy em nosso projeto?
answer: Gerenciar a conexão com o banco de dados
answer: Representar o modelo dos dados como objetos
answer: Fazer busca de dados no banco
answer-correct: Todas as alternativas
content:
<?/quiz?>

<?quiz?>
question: 02 - O Registry do sqlalchemy tem a função de:
answer: Criar um schema de validação da API
answer-correct: Criar um objeto que representa a tabela no banco de dados
answer: Criar um registro no banco de dados
content:
<?/quiz?>

<?quiz?>
question: 03 - Qual a função do objeto Mapper
answer: executar a função map do python no banco de dados
answer-correct: Criar uma relação entre o tipo de dados do python e o da tabela do banco
answer: Dizer qual o tipo de dado que terá no banco de dados
answer: Fazer uma conversão para tipos do python
content:
<?/quiz?>

<?quiz?>
question: 04 - O que faz o a função mapped_column?
answer: Indicar valores padrões para as colunas
answer: Criar indicadores de SQL no objeto
answer: Adiciona restrições referentes a coluna no banco de dados
answer-correct: Todas as anteriores
content:
<?/quiz?>

```quiz
{
    "questao": "05 - Qual a função do mapped_column no seguinte código:",
	"opcoes": {
		"a": "O valor de quiz deve ser único na coluna",
		"b": "Este campo é o único da tabela",
		"c": "A tabela só tem um campo",
		"d": "Só é possível inserir um valor único nesse campo",
	},
	"correta": "a",
	"code" : """
```python
quiz: Mapped[str] = mapped_column(unique=True)
```"""
}
```

<?quiz?>
question: 06 - O que significa init=False no mapeamento?
answer: Diz que a coluna não deve ser iniciada no banco
answer-correct: Toma a responsabilidade do preenchimento do campo para o SQLAlchemy
answer: Diz que existe um valor padrão na coluna
content:
<?/quiz?>

```quiz
{
    "questao": '07 - O método "scalar" da session tem o objetivo de:',
	"opcoes": {
		"a": "Executar uma query no banco de dados",
		"b": "Retornar somente um resultado do banco",
		"c": "Converter o resultado da query em um objeto do modelo",
		"d": "Todas as alternativas estão corretas",
	},
	"correta": "d",
	"code" : """
```python
session.scalar(select(User).where(User.username == 'Quiz'))
```"""
}
```

```quiz
{
    "questao": '08 - A função "select" tem a objetivo de:',
	"opcoes": {
		"a": "Executar uma busca no banco de dados",
		"b": "Selecionar objetos 'User' no projeto",
		"c": "Montar uma query de SQL",
		"d": "Criar um filtro de busca",
	},
	"correta": "c",
	"code" : """
```python
session.scalar(select(User).where(User.username == 'Quiz'))
```"""
}
```

<?quiz?>
question: 09 - Qual o objetivo do arquivo .env?
answer-correct: Isolar variáveis do ambiente do código fonte
answer: Criar variáveis no ambiente virtual
answer: Criar variáveis globais no projeto
content:
<?/quiz?>

<?quiz?>
question: 10 - As migrações têm a função de:
answer: Refletir as tabelas do banco de dados no ORM
answer: Criar tabelas no banco de dados
answer-correct: Refletir as classes do ORM no banco de dados
answer: Criar um banco de dados
content:
<?/quiz?>
