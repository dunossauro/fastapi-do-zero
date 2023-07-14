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


## Aula 6: Autenticação e Autorização em FastAPI

- Criação de rotas para registrar e logar usuários
- Implementação da autenticação e restrições de acesso
- Escrita e execução dos testes para autenticação e restrições de acesso

### Youtube

Descrição: Neste vídeo, vamos dar um passo além na segurança da nossa API. Vamos aprender como proteger endpoints específicos em FastAPI e como lidar com a autorização. Também vamos atualizar nossos testes para refletir essas mudanças. Se você deseja criar APIs robustas e seguras, esta aula é para você. Junte-se a nós nessa jornada de aprender FastAPI!

Tags:FastAPI, Python, Autenticação FastAPI, Autorização FastAPI, Proteção de endpoints FastAPI, Testes em FastAPI, Desenvolvimento Web com Python, APIs Rest com Python, Desenvolvimento Back-end com Python, JWT em FastAPI.



## Aula 7: Refatoração em FastAPI: Implementando Routers e Variáveis de Ambiente

- Reestruturar o projeto para facilitar sua manutenção
- Criação de routers
- Remover constante dos códigos

### youtube

Descrição: Neste vídeo, exploramos algumas das melhores práticas de desenvolvimento com o FastAPI, refatorando nossa aplicação para utilizar routers e variáveis de ambiente. Abordamos a criação e utilização de routers para organizar melhor nosso código e discutimos a importância de manter constantes sensíveis, como chaves secretas, fora do código, utilizando variáveis de ambiente. Se você está interessado em melhorar sua habilidade com o FastAPI e em entender algumas das melhores práticas de desenvolvimento, este vídeo é para você.

Tags: FastAPI, Python, Desenvolvimento Web, API, Rest API, FastAPI Router, Variáveis de Ambiente, Refatoração, Melhores Práticas, Desenvolvimento Python, OpenAI, Pydantic, SQLAlchemy, Autenticação JWT, TDD, Clean Code


## Aula 8: Autenticação JWT e Testes de Casos de Borda


- Testar os casos de autenticação de forma correta
- Implementar o refresh do token
- Introduzir testes que param o tempo com freezefun
- Introduzir geração de modelos automática com factory-boy

### youtube

Descrição: Nesta aula, continuamos a desenvolver nossa API REST usando FastAPI e PyTest. Damos um grande passo em direção à segurança do nosso sistema implementando a autenticação JWT (JSON Web Tokens). Aprenda como criar tokens, refrescar tokens, e o que acontece quando esses tokens expiram. Além disso, reforçamos a importância dos testes automatizados, cobrindo vários cenários marginais. Acompanhe-nos nesta jornada para desenvolver uma API robusta e segura.

Tags: Python, FastAPI, API REST, Autenticação, JWT, JSON Web Tokens, Testes, PyTest, TDD, Desenvolvimento de Software, Programação, Casos de Borda, Segurança de Aplicações, Backend, Desenvolvimento Backend, Desenvolvimento Web

# [PARA REVISÃO]

## Aula 9: Criando Rotas CRUD para Tarefas em FastAPI

- Criação das rotas para as operações CRUD das tarefas
- Fazer com só o usuário dono da tarefa possa acessar e modificar suas tarefas
- Escrita e execução dos testes para cada operação das tarefas

### Youtube

Descrição: Hoje, vamos focar em como criar rotas CRUD eficientes para as tarefas em nosso projeto FastAPI. Este é um passo fundamental para construir qualquer API e vamos guiá-lo por cada etapa do processo.

Tags: FastAPI, Python, CRUD FastAPI, API de Tarefas, Desenvolvimento de API, Desenvolvimento web com Python

## Aula 10: Dockerizando sua Aplicação FastAPI

- Explicação básica do Docker e sua utilidade
- Escrita do Dockerfile para a aplicação
- Demonstração de como construir e executar a aplicação com Docker
- Testes para garantir que a aplicação funciona corretamente quando dockerizada

### Youtube

Descrição: Já ouviu falar sobre Docker mas nunca soube como usá-lo em seu projeto? Nesta aula, vamos dockerizar nossa aplicação FastAPI, um passo essencial para tornar nosso deploy mais fácil e eficiente.

Tags: FastAPI, Python, Docker, FastAPI com Docker, Deploy de API, Desenvolvimento web com Python

## Aula 11: Automatizando Testes com GitHub Actions e FastAPI

- Introdução aos conceitos de CI/CD e sua importância
- Explicação sobre o papel do Github Actions na CI/CD
-Configuração do Github Actions para executar testes automaticamente em cada push


### Youtube

Descrição: Continuando nosso curso de FastAPI, vamos automatizar nossos testes com o GitHub Actions. Esta ferramenta nos permite realizar testes sempre que fizermos push para nosso repositório, garantindo que nossas alterações não quebrem nossa aplicação.

Tags: FastAPI, Python, GitHub Actions, CI/CD, Automatização de Testes, Desenvolvimento web com Python

## Aula 12: Fazendo Deploy de sua Aplicação FastAPI com Fly.io

- Breve introdução ao Fly.io
- Demonstração de como configurar e fazer o deploy da aplicação usando o Fly.io
- Discussão sobre possíveis problemas de deploy e como resolvê-los

### Youtube

Descrição: Estamos quase lá! Neste vídeo, vamos fazer deploy de nossa aplicação FastAPI usando o Fly.io. Aprenda a levar sua API da fase de desenvolvimento para a produção de maneira eficiente.

Tags: FastAPI, Python, Fly.io, Deploy FastAPI, Deploy de API, Desenvolvimento web com Python

## Aula 13: Conclusão do Curso de FastAPI - Revisão e Próximos Passos

- Revisão dos principais pontos aprendidos durante o curso
- Discussão sobre possíveis extensões ou melhorias para o projeto
- Conclusão e encerramento do curso

### Youtube

Descrição: Parabéns por chegar até aqui! Neste último vídeo do nosso curso de FastAPI, vamos revisar o que aprendemos e discutir sobre os próximos passos. Explore possíveis melhorias e extensões para o seu projeto FastAPI.

Tags: FastAPI, Python, Revisão de FastAPI, Conclusão do Curso, Próximos Passos em FastAPI, Desenvolvimento web com Python
