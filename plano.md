# FastAPI do Zero: Criando um projeto com Bancos de dados, Testes e Deploy

## Aula 1: Introdução ao Curso de FastAPI - O que você vai aprender?

- Apresentação pessoal e do curso
- Explicação do projeto e das tecnologias que serão usadas
- Discussão sobre os objetivos e expectativas do curso
- Explicação do formato e estrutura do curso

### Youtube

Descrição: Boas-vindas à primeira aula prática do nosso curso "FastAPI do Zero: Criando um Projeto com Bancos de Dados, Testes e Deploy". Neste vídeo, iniciaremos o curso configurando o ambiente de desenvolvimento, introduzindo e instalando as ferramentas essenciais para começar a desenvolver com FastAPI. Vamos mergulhar na instalação do Python 3.11, na configuração do gerenciador de pacotes Poetry, na criação do nosso primeiro projeto FastAPI e, finalmente, na configuração de ferramentas de desenvolvimento e testes como Ruff, Blue, Isort, Pytest e Taskipy. Juntos, daremos os primeiros passos na escrita de testes com Pytest e na inicialização do nosso repositório Git.

Tags: FastAPI, Python, Curso de FastAPI, Introdução ao FastAPI, APIs com Python, Desenvolvimento web com Python, Configuração do ambiente FastAPI, Desenvolvimento Orientado por Testes, TDD com FastAPI, Pytest, Ruff, Blue, Isort, Taskipy, Poetry, Git, Hello World em FastAPI.


## Aula 2: Configurando o Ambiente de Desenvolvimento para FastAPI

- Introdução ao ambiente de desenvolvimento (IDE, terminal, etc.)
- Instalação do FastAPI e suas dependências
- Configuração das ferramentas de desenvolvimento
- Execução do primeiro "Hello, World!" com FastAPI

### Youtube

Descrição: Continuamos nossa jornada no mundo do FastAPI neste vídeo, onde você aprenderá a verificar e corrigir erros de formatação no seu código usando ferramentas como taskipy, blue e ruff. Você também será apresentado à biblioteca pytest e como usá-la para escrever seu primeiro teste unitário em FastAPI. Finalmente, você verá como verificar a cobertura de teste do seu código com a biblioteca coverage e como visualizar esses resultados de uma forma mais intuitiva. Não esqueça de configurar seu repositório Git ao final da aula!

Tags: FastAPI, Python, Taskipy, Blue, Ruff, Pytest, Testes Unitários, Coverage, Cobertura de Testes, Git, Ambiente de Desenvolvimento Python, Desenvolvimento web com Python, Desenvolvimento Orientado por Testes, Teste de API

## Aula 3: Estruturando seu Projeto FastAPI e Criando Rotas CRUD

- Entendimento dos verbos HTTP e códigos de resposta
- Compreender a estrutura de um projeto FastAPI e como estruturar rotas CRUD (Criar, Ler, Atualizar, Deletar)
- Aprender sobre a biblioteca Pydantic e sua utilidade na validação e serialização de dados
- Implementação de rotas CRUD em FastAPI
- Escrita e execução de testes para validar o comportamento das rotas

### Youtube

Descrição: Nesta Aula 3 do curso "FastAPI do Zero: Criando um Projeto com Bancos de Dados, Testes e Deploy", vamos explorar a estruturação do nosso projeto FastAPI e implementar todas as rotas CRUD (Criar, Ler, Atualizar e Deletar) para o nosso recurso de usuário. Você vai aprender sobre os verbos HTTP, os códigos de resposta, a estrutura de um projeto FastAPI, a biblioteca Pydantic, e muito mais. Ao final desta aula, você será capaz de criar suas próprias rotas CRUD em FastAPI, e entenderá a importância de escrever e executar testes para validar o comportamento das rotas.

Tags: FastAPI, Python, APIs, Desenvolvimento Web, Backend, HTTP, CRUD, Testes, Pydantic, Rotas CRUD, Verbos HTTP, Códigos de Resposta HTTP, Estrutura de Projetos FastAPI, Serialização de Dados, Validade de Dados, Desenvolvimento de Software, Programação.

## Aula 4: Configurando Banco de Dados e Gerenciando Migrações com Alembic

-  Introdução ao SQLAlchemy e Alembic
-  Instalando SQLAlchemy e Alembic
-  Configurando e criando o banco de dados
-  Criando e localizando tabelas utilizando SQLAlchemy
-  Testando a criação de tabelas
-  Gerenciando migrações do banco de dados com Alembic

### Youtube

Descrição: Boas-vindas à quarta aula do nosso curso "FastAPI do Zero: Criando um Projeto com Bancos de Dados, Testes e Deploy". Hoje, nosso foco é a criação do banco de dados e gerenciamento de migrações com SQLAlchemy e Alembic. Nós vamos conduzi-los através de cada passo necessário para instalar o SQLAlchemy e Alembic, configurar o ambiente do banco de dados, criar tabelas e gerenciar migrações. E, é claro, vamos continuar com nossa abordagem de Desenvolvimento Orientado por Testes, mostrando como escrever e executar testes para o seu banco de dados. Venha conosco e aprenda mais sobre o poderoso FastAPI e como gerenciar eficientemente seus dados.

Tags: FastAPI, Python, SQLAlchemy, Alembic, Gerenciamento de Banco de Dados com FastAPI, Migração de Dados com Alembic, Desenvolvimento Web com Python, Testes de Banco de Dados, Desenvolvimento Orientado por Testes, FastAPI do Zero.

## Aula 5: Integrando Banco de Dados ao FastAPI

- Integrando SQLAlchemy à nossa aplicação FastAPI
- Utilizando a função Depends para gerenciar dependências
- Modificando endpoints para interagir com o banco de dados
- Criando novos schemas
- Testando os novos endpoints com Pytest e fixtures

### Youtube

Descrição: Boas-vindas à quinta aula da nossa série "FastAPI do Zero"! Nesta aula, elevamos a complexidade do nosso projeto, integrando o SQLAlchemy à nossa aplicação FastAPI e substituindo nosso banco de dados temporário por um banco de dados SQL robusto.

Aqui, nós exploramos o poder da função Depends do FastAPI para gerenciar as sessões do banco de dados, garantindo que cada request tenha sua própria sessão. Além disso, remodelamos nossos schemas Pydantic para que possam trabalhar harmoniosamente com o SQLAlchemy, otimizando a interação com o banco de dados.

Também revisamos nossos endpoints, atualizando-os para que possam efetivamente manipular as operações do banco de dados. Para assegurar que nossas mudanças estão funcionando como esperado, utilizamos o Pytest juntamente com fixtures, criando um ambiente de teste controlado.

Tags: FastAPI, Python, API, Desenvolvimento Web, SQLAlchemy, Depends, Pydantic, Pytest, Fixtures, Endpoints, Banco de Dados, APIs RESTful, Desenvolvimento de APIs, Gerenciamento de Dependências, Teste de Software, Banco de Dados SQL, Integração de Banco de Dados, Testes Unitários.


# [PARA REVISÃO]
## Aula 6: Autenticação e Autorização em FastAPI

- Criação de rotas para registrar e logar usuários
- Implementação da autenticação e restrições de acesso
- Escrita e execução dos testes para autenticação e restrições de acesso

### Youtube

Descrição: A segurança é fundamental em qualquer API. Neste vídeo, você aprenderá a implementar autenticação e autorização em seu projeto FastAPI. Vamos construir juntos rotas seguras para registrar e logar usuários.

Tags: FastAPI, Python, Autenticação FastAPI, Autorização FastAPI, Segurança em APIs, Desenvolvimento web com Python

## Aula 7: Criando Rotas CRUD para Tarefas em FastAPI

- Criação das rotas para as operações CRUD das tarefas
- Escrita e execução dos testes para cada operação das tarefas

### Youtube

Descrição: Hoje, vamos focar em como criar rotas CRUD eficientes para as tarefas em nosso projeto FastAPI. Este é um passo fundamental para construir qualquer API e vamos guiá-lo por cada etapa do processo.

Tags: FastAPI, Python, CRUD FastAPI, API de Tarefas, Desenvolvimento de API, Desenvolvimento web com Python

## Aula 8: Maximizando a Cobertura de Testes em FastAPI com Coverage

- Introdução ao conceito de cobertura de testes e sua importância
- Demonstração de como usar o coverage para medir a cobertura de testes
 - Revisão e melhoria dos testes com base na análise de cobertura
 
### Youtube

Descrição: Testes são cruciais para garantir que sua API FastAPI funcione como esperado. Neste vídeo, ensinaremos você a usar a ferramenta 'coverage' para analisar a cobertura de seus testes e melhorar a qualidade do seu código.

Tags: FastAPI, Python, Testes FastAPI, Coverage, TDD, Desenvolvimento web com Python

## Aula 9: Dockerizando sua Aplicação FastAPI

- Explicação básica do Docker e sua utilidade
- Escrita do Dockerfile para a aplicação
- Demonstração de como construir e executar a aplicação com Docker
- Testes para garantir que a aplicação funciona corretamente quando dockerizada

### Youtube

Descrição: Já ouviu falar sobre Docker mas nunca soube como usá-lo em seu projeto? Nesta aula, vamos dockerizar nossa aplicação FastAPI, um passo essencial para tornar nosso deploy mais fácil e eficiente.

Tags: FastAPI, Python, Docker, FastAPI com Docker, Deploy de API, Desenvolvimento web com Python

## Aula 10: Automatizando Testes com GitHub Actions e FastAPI

- Introdução aos conceitos de CI/CD e sua importância
- Explicação sobre o papel do Github Actions na CI/CD
-Configuração do Github Actions para executar testes automaticamente em cada push


### Youtube

Descrição: Continuando nosso curso de FastAPI, vamos automatizar nossos testes com o GitHub Actions. Esta ferramenta nos permite realizar testes sempre que fizermos push para nosso repositório, garantindo que nossas alterações não quebrem nossa aplicação.

Tags: FastAPI, Python, GitHub Actions, CI/CD, Automatização de Testes, Desenvolvimento web com Python

## Aula 11: Fazendo Deploy de sua Aplicação FastAPI com Fly.io

- Breve introdução ao Fly.io
- Demonstração de como configurar e fazer o deploy da aplicação usando o Fly.io
- Discussão sobre possíveis problemas de deploy e como resolvê-los

### Youtube

Descrição: Estamos quase lá! Neste vídeo, vamos fazer deploy de nossa aplicação FastAPI usando o Fly.io. Aprenda a levar sua API da fase de desenvolvimento para a produção de maneira eficiente.

Tags: FastAPI, Python, Fly.io, Deploy FastAPI, Deploy de API, Desenvolvimento web com Python

## Aula 12: Conclusão do Curso de FastAPI - Revisão e Próximos Passos

- Revisão dos principais pontos aprendidos durante o curso
- Discussão sobre possíveis extensões ou melhorias para o projeto
- Conclusão e encerramento do curso

### Youtube

Descrição: Parabéns por chegar até aqui! Neste último vídeo do nosso curso de FastAPI, vamos revisar o que aprendemos e discutir sobre os próximos passos. Explore possíveis melhorias e extensões para o seu projeto FastAPI.

Tags: FastAPI, Python, Revisão de FastAPI, Conclusão do Curso, Próximos Passos em FastAPI, Desenvolvimento web com Python
