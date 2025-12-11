# 04 - Configurando o Banco de Dados e Gerenciando Migrações com Alembic

<quiz>
Qual a função do sqlalchemy em nosso projeto?
- [ ] Gerenciar a conexão com o banco de dados
- [ ] Representar o modelo dos dados como objetos
- [ ] Fazer busca de dados no banco
- [x] Todas as alternativas
</quiz>

<quiz>
O Registry do sqlalchemy tem a função de:
- [ ] Criar um schema de validação da API
- [x] Criar um objeto que representa a tabela no banco de dados
- [ ] Criar um registro no banco de dados
</quiz>

<quiz>
Qual a função do objeto `Mapped`
- [ ] executar a função map do python no banco de dados
- [x] Criar uma relação entre o tipo de dados do python e o da tabela do banco
- [ ] Dizer qual o tipo de dado que terá no banco de dados
- [ ] Fazer uma conversão para tipos do python
</quiz>

<quiz>
O que faz a função `mapped_column`?
- [ ] Indicar valores padrões para as colunas
- [ ] Criar indicadores de SQL no objeto
- [ ] Adiciona restrições referentes a coluna no banco de dados
- [x] Todas as anteriores
</quiz>

<quiz>
Qual a função do `mapped_column` no seguinte código:

```python
quiz: Mapped[str] = mapped_column(unique=True)
```

- [x] O valor de quiz deve ser único na coluna
- [ ] Este campo é o único da tabela
- [ ] A tabela só tem um campo
- [ ] Só é possível inserir um valor único nesse campo
</quiz>

<quiz>
O que significa `init=False` no mapeamento?
- [ ] Diz que a coluna não deve ser iniciada no banco
- [x] Toma a responsabilidade do preenchimento do campo para o SQLAlchemy
- [ ] Diz que existe um valor padrão na coluna
</quiz>

<quiz>
O método `.scalar` da `session` tem o objetivo de:

```python
session.scalar(select(User).where(User.username == 'Quiz'))
```

- [ ] Executar uma query no banco de dados
- [ ] Retornar somente um resultado do banco
- [ ] Converter o resultado da query em um objeto do modelo
- [x] Todas as alternativas estão corretas
</quiz>

<quiz>
A função `select` tem o objetivo de:

```python
session.scalar(select(User).where(User.username == 'Quiz'))
```

- [ ] Executar uma busca no banco de dados
- [ ] Selecionar objetos `User` no projeto
- [x] Montar uma query de SQL
- [ ] Criar um filtro de busca
</quiz>


<quiz>
Qual o objetivo do arquivo `.env`?
- [x] Isolar variáveis do ambiente do código fonte
- [ ] Criar variáveis no ambiente virtual
- [ ] Criar variáveis globais no projeto
</quiz>

<quiz>
As migrações têm a função de:
- [ ] Refletir as tabelas do banco de dados no ORM
- [ ] Criar tabelas no banco de dados
- [x] Refletir as classes do ORM no banco de dados
- [ ] Criar um banco de dados
</quiz>
