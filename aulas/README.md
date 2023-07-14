# [WIP] FastAPI do ZERO

> Ainda está em uma fase bastante embrionária esse arquivo!

## Criando um Projeto com Bancos de Dados, Testes e Deploy

Olá a todos e boas vindas ao curso "FastAPI do Zero: Criando um Projeto com Bancos de Dados, Testes e Deploy". Nessa aula vamos abordar o que você pode esperar aprender neste curso e como ele está estruturado. Então, sem mais delongas, vamos começar!

## O que é FastAPI?

FastAPI é um framework Python moderno e rápido (alta performance) para construção de APIs, que é fácil de aprender e traz inúmeros benefícios. FastAPI aproveita as anotações de tipo Python para fornecer uma experiência incrivelmente eficiente para desenvolver APIs RESTful.

## Sobre o curso

Este curso foi criado com um propósito em mente: ajudar desenvolvedores, tanto iniciantes quanto experientes, a entender e utilizar o FastAPI para construir APIs. Durante as aulas, construiremos um projeto prático de gerenciamento de tarefas (um todo list), com autenticação de usuários e todas as operações CRUD (criar, ler, atualizar, deletar).

{dizer que iremos usar as ferramentas mais atualizadas nesse momento (em 2023). As versões que quebraram retrocompatibilidade como o fastapi 0.100, o sqlalchemy ORM 2.0 e o pydantic 2.0. E que também usaremos a versão 3.11 do python. Também mencionar que vamos usar o alembic para gerir migrações e a parte mais importante é que vamos usar o pytest, lidar com cobertura de código e testes a todo momento}


## O que você vai aprender?

### Ao longo deste curso, vamos cobrir os seguintes tópicos:

1. Configura um ambiente de desenvolvimento para FastAPI: Para garantir que todos estão na mesma página, começaremos do zero, configurando nosso ambiente de desenvolvimento.

2. Primeiros Passos com FastAPI e TDD: Após a configuração do ambiente, começaremos a explorar a estrutura básica de um projeto FastAPI, juntamente com uma introdução ao Desenvolvimento Orientado a Testes (TDD).

3. Modelagem de Dados com Pydantic e SQLAlchemy: Abordaremos como criar e manipular modelos de dados com Pydantic e SQLAlchemy, duas bibliotecas poderosas que tornam o FastAPI ainda mais eficaz.

4. Autenticação e Autorização em FastAPI: Ensinar-lhe-emos a construir um sistema de autenticação para proteger suas rotas e garantir que apenas usuários autenticados possam acessar dados específicos.

5. Testando sua Aplicação FastAPI: Uma introdução completa ao teste de sua aplicação FastAPI com o pytest e coverage.

6. Dockerizando e Fazendo Deploy de sua Aplicação FastAPI: Por fim, vamos cobrir como dockerizar sua aplicação FastAPI e como fazer o deploy dela usando Fly.io.

## Pré-requisitos

Para aproveitar ao máximo este curso, é recomendado que você tenha algum conhecimento prévio de Python. Além disso, algum entendimento básico de desenvolvimento web e APIs RESTful será útil, mas não essencial, pois {dizer que a ideia é fazer um projeto com foco prático, então você pode entender como as coisas são construídas até o fim do processo!}

??? info "Caso esteja iniciando seus estudos em Python!"
	Caso você ainda não se sinta uma pessoa preparada, ou caiu aqui sem saber exatamente o que esperar. Temos um pequeno curso introdutório. Destinado aos primeiros passos com python.
	![type:video](https://youtube.com/embed/yTQDbqmv8Ho)
	
	Ou então a leitura do [Pense em python](https://penseallen.github.io/PensePython2e/){:target="_blank"}

## Aulas

1. [Configurando o Ambiente de Desenvolvimento](/01/){:target="_blank"}
2. [Estruturando seu Projeto e Criando Rotas CRUD](/02/){:target="_blank"}
3. [Configurando Banco de Dados e Gerenciando Migrações com Alembic](/03/){:target="_blank"}
4. [Integrando Banco de Dados a API](/04/){:target="_blank"}
5. [Autenticação e Autorização](/05/){:target="_blank"}
6. [Refatorando a Estrutura do Projeto](/06/){:target="_blank"}
7. [Tornando o sistema de autenticação robusto](/07/){:target="_blank"}
8. [Criando Rotas CRUD para Gerenciamento de Tarefas em FastAPI](/08/){:target="_blank"}
9. [Criando Rotas CRUD para Tarefas](/09/){:target="_blank"}
10. [Dockerizando a aplicação](/10/){:target="_blank"}
11. [Automatizando os testes com integração contínua](/11/){:target="_blank"}
12. [Fazendo o deploy no fly.io](/11/){:target="_blank"}
13. [Despedida](/12/){:target="_blank"}

### 🦖 Quem vai ministrar essas aulas?

Prazer! Eu me chamo Eduardo. Mas as pessoas me conhecem na internet como [@dunossauro](https:/dunossauro.com){:target="_blank"}.

<div class="sbs" markdown>
![Uma fotografia minha, Dunossauro, sentado em um banco com um por do sol ao fundo](assets/dunossauro.jpg){ align=left width="300" .shadow}
<div markdown>

Eu sou um programador Python muito empolgado e curioso. Toco um projeto pessoal chamado [Live de Python](https://www.youtube.com/@Dunossauro){:target="_blank"} a pouco mais de 6 anos. Onde conversamos sobre tudo e mais um pouco quando o assunto é python.

Esse projeto que estamos desenvolvendo é um pedaço, um projeto, de um grande curso de fastAPI que estou montando. Espero que você se divirta ao máximo com a parte prática enquanto escrevo em mais detalhes todo o potencial teórico que lançarei no futuro!

[Caso queira saber mais sobre esse projeto completo](https://youtu.be/ikmFLkjxqFg){:target="_blank"}.
</div>
</div>

## 📖 Licença

Todo esse curso foi escrito e produzido por Eduardo Mendes ([@dunossauro](https://dunossauro.com/){:target="_blank"}).

Todo esse material é gratuito e está sob licença Creative Commons [BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/){:target="_blank"}. O que quer dizer que:

- Você pode copiar e reproduzir esse material em qualquer meio e em qualquer formato;
- Você pode adaptar esse material e construir outros materiais usando esse material.

Pontos de atenção:

- Você precisa dar os devidos créditos a esse material onde for usar ou adaptar;
- Você não pode usar para fins comerciais. Como vender ou usar para obter vantagens comerciais;
- Todo o material derivado desse material deve ser redistribuído com a licença [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/){:target="_blank"}.

## 🧰 Ferramentas necessárias para acompanhar o curso

1. Um editor de texto ou IDE de sua escolha. Estou usando o [GNU/Emacs](https://www.gnu.org/software/emacs/){:target="_blank"} enquanto escrevo as aulas;
2. Um terminal. Todos os exemplos do curso são executados e explicados no terminal. Você pode usar o que se sentir mais a vontade e for compatível com seu sistema operacional;
3. Ter o interpretador Python instalado em uma versão igual ou superior a `3.11`
4. Uma conta no [Github](https://github.com/){:target="_blank"}: para podermos testar com github Actions;
5. Uma conta no [Fly.io](https://fly.io/){:target="_blank"}: ferramenta que usaremos para fazer deploy.

## 🔧 Ferramentas de apoio

Toda essa página foi feita usando as seguintes bibliotecas:

- [MkDocs](https://www.mkdocs.org/){:target="_blank"}: Para geração das páginas estáticas usando Markdown
- [Mkdocs-material](https://squidfunk.github.io/mkdocs-material/){:target="_blank"}: Tema para o MKDocs
- [pymdown-extensions](https://facelessuser.github.io/pymdown-extensions/){:target="_blank"}: Extensões para MKDocs, como emojis, diagramas e blocos estilizados de código
- [Python-Markdown](https://python-markdown.github.io/){:target="_blank"}: Extensão do Python para Markdown
- [Mkdocs-video](https://github.com/soulless-viewer/mkdocs-video){:target="_blank"}: Extensão para o MKDocs exibir os vídeos na página
- [Mermaid.js](https://mermaid-js.github.io/mermaid/){:target="_blank"}: Construção dos diagramas

### 📁 Repositório
O versionamento de tudo está sendo feito no [repositório do curso Github](https://github.com/dunossauro/fastapi-do-zero){:target="_blank"}

### 🚀 Deploy
Os deploys das páginas estáticas geradas pelo MkDocs estão sendo feitos no [Netlify](https://www.netlify.com/){:target="_blank"}

## Conclusão

Estou muito animados para começar esta jornada com você. Se você está pronto para aprender como construir APIs web eficientes e testáveis, então este é o curso certo para você. Fique atento para a primeira aula, onde vamos configurar nosso ambiente de desenvolvimento e dar os primeiros passos com FastAPI e TDD!
