---
title: FastAPI do Zero!
description: Boas vindas ao nosso minicurso de FastAPI!
---

<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
<lottie-player src="https://raw.githubusercontent.com/dunossauro/fastapi-do-zero/main/stuff/anim_lottie.json" background="transparent" speed="1" style="margin-left: auto; margin-right: auto;" loop autoplay></lottie-player>

# FastAPI do ZERO

{%set aula = "00" %}
{%set link = "QShMRcicxnE" %}


??? tip "Caso prefira ver a apresentação do curso em vídeo"
	Esse aula ainda não está disponível em formato de vídeo, somente em texto ou live!
	![type:video](https://www.youtube.com/embed/{{link}})

	[Aula :fontawesome-brands-youtube:](https://youtu.be/{{link}}?list=PLOQgLBuj2-3IuFbt-wJw2p2NiV9WTRzIP){ .md-button }
	[Slides :fontawesome-solid-file-powerpoint:](https://github.com/dunossauro/fastapi-do-zero/blob/main/slides/pdf/aula_{{aula}}.pdf){ .md-button }

> Esse material passa por atualizações periódicas. Você pode acompanhar as notas de alterações [aqui](/alteracoes/){:target="_blank"}

Olá, boas vindas ao curso de FastAPI!

A nossa intenção neste curso é facilitar o aprendizado no desenvolvimento de APIs usando o FastAPI. Vamos explorar como integrar bancos de dados, criar testes e um sistema básico de autenticação com JWT. Tudo isso para oferecer uma boa base para quem quer trabalhar com desenvolvimento web com Python. A ideia desse curso é apresentar os conceitos de forma prática, construindo um projeto do zero e indo até a sua fase de produção.


## O que é FastAPI?

[FastAPI](https://fastapi.tiangolo.com/){:target="_blank"} é um framework Python moderno, projetado para simplicidade, velocidade e eficiência. A combinação de diversas funcionalidades modernas do Python como anotações de tipo e suporte a concorrência, facilitando o desenvolvimento de APIs.

## Sobre o curso

Este curso foi desenvolvido para oferecer uma experiência prática no uso do FastAPI, uma das ferramentas mais modernas para construção de APIs. Ao longo do curso, o objetivo é que você obtenha uma compreensão das funcionalidades do FastAPI e de boas práticas associadas a ele.

O projeto central do curso será a construção de um gerenciador de tarefas (uma lista de tarefas), começando do zero. Esse projeto incluirá a implementação da autenticação do usuário e das operações CRUD completas.

Para a construção do projeto, serão utilizadas as versões mais recentes das ferramentas, disponíveis em 2025, como a versão 0.115 do FastAPI, a versão 2.0+ do Pydantic, a versão 2.0+ do SQLAlchemy ORM, além do Python 3.11/3.12 e do Alembic para gerenciamento de migrações.

Além da construção do projeto, o curso também incluirá a prática de testes, utilizando o pytest. Essa abordagem planeja garantir que as APIs desenvolvidas sejam não apenas funcionais, mas também robustas e confiáveis.

## O que você vai aprender?

Aqui está uma visão geral dos tópicos que abordaremos neste curso:

1. **Configuração do ambiente de desenvolvimento para FastAPI**: começaremos do absoluto zero, criando e configurando nosso ambiente de desenvolvimento.

2. **Primeiros Passos com FastAPI e Testes**: após configurar o ambiente, mergulharemos na estrutura básica de um projeto FastAPI e faremos uma introdução detalhada ao Test Driven Development (TDD).

3. **Modelagem de Dados com Pydantic e SQLAlchemy**: aprenderemos a criar e manipular modelos de dados utilizando Pydantic e SQLAlchemy, dois recursos que levam a eficiência do FastAPI a outro nível.

4. **Autenticação e Autorização em FastAPI**: construiremos um sistema de autenticação completo, para proteger nossas rotas e garantir que apenas usuários autenticados tenham acesso a certos dados.

5. **Testando sua Aplicação FastAPI**: faremos uma introdução detalhada aos testes de aplicação FastAPI, utilizando as bibliotecas pytest e coverage. Além de executá-los em um pipeline de integração contínua com github actions.

6. **Dockerizando e Fazendo Deploy de sua Aplicação FastAPI**: por fim, aprenderemos como "dockerizar" nossa aplicação FastAPI e fazer seu deploy utilizando Fly.io.

## 💰 Esse curso é gratuito?

SIM! Esse curso foi todo desenvolvido [de forma aberta](#licenca){:target="_blank"} e com a [ajuda financeira](https://apoia.se/fastapi){:target="_blank"} de pessoas incríveis. Caso você sinta vontade de contribuir, você pode me pagar um café por pix (pix.dunossauro@gmail.com) ou apoiar a [campanha recorrente de financiamento coletivo da live de python](https://apoia.se/livedepython){:target="_blank"} que é o que paga as contas aqui de casa.

## Onde o curso será disponibilizado?

Esse material será disponibilizado de três formas diferentes:

1. Em livro texto: todo o material está disponível nessa página;

2. Em aulas síncronas ao vivo: para quem prefere o compromisso de acompanhar em grupo. [**Datas já disponíveis**](aulas/sincronas.md);

    **Playlist das Aulas síncronas (Ao vivo)**:
	<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?si=bbzMgz9dXoVXNdlR&amp;list=PLOQgLBuj2-3IuFbt-wJw2p2NiV9WTRzIP" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

3. Em formato de vídeo (assíncronas): todas as aulas serão disponibilizadas em formato de vídeo em meu canal do [YouTube](http://youtube.com/@dunossauro){:target="_blank"} para quem prefere assistir ao ler. (**Vídeos ainda não disponíveis**)

## Pré-requisitos

Para aproveitar ao máximo este curso, é recomendado que você já tenha algum conhecimento prévio em python, se pudesse listar o que considero importante para não se perder, os tópicos em python importantes são:

- O funcionamento de funções: como criar e usar ([referência](https://youtu.be/0yXPQZvlgrk){:target="_blank"});
- O funcionamento das estruturas de dados: como listas, dicionários e etc;
- Uma pitada sobre objetos: saber o que são métodos e atributos ([referência](https://youtu.be/BALM_oJcJL4){:target="_blank"});
- Classes de dados: o funcionamento básico das dataclasses ([referência](https://youtu.be/NtZY3AmsBSk){:target="_blank"}).

> As referências servem como base caso você ainda não tenha estudado esses assuntos

Alguns outros tópicos não relativos a python também serão abordados. Então é interessante que você tenha algum entendimento básico sobre: 

- Desenvolvimento Web e APIs RESTful: não essencial, pois iremos abordar, mas o quanto mais você souber melhor para acompanhar;
- Banco de dados / SQL: Um conhecimento básico sobre criação e busca de dados usando SQL já o suficiente, embora esse tópico também seja como o anterior, quanto mais você souber melhor;
- git: não nos aprofundaremos nesse tópico durante o curso, mas usaremos operações básicas de git (como commit e push);
- docker: também não nos aprofundaremos nesse tópico e ele só será abordado nas aulas finais. Mas, também, só usaremos comandos básicos de docker e docker-compose.

??? info "Caso esteja iniciando seus estudos em Python!"
	Caso você ainda não se sinta uma pessoa preparada, ou caiu aqui sem saber exatamente o que esperar. Temos um pequeno curso introdutório. Destinado aos primeiros passos com python.
	![type:video](https://youtube.com/embed/yTQDbqmv8Ho)

	[:fontawesome-brands-youtube: Link direto](https://www.youtube.com/watch?v=yTQDbqmv8Ho){ .md-button }

	Também temos uma live focada em dicas para iniciar os estudos em python

    ![type:video](https://www.youtube.com/embed/HSotf1Amess)

	[:fontawesome-brands-youtube: Link direto](https://www.youtube.com/watch?v=HSotf1Amess){ .md-button }

	Ou então a leitura do livro [**Pense em python**](https://penseallen.github.io/PensePython2e/){:target="_blank"}

## Aulas

1. [Configurando o Ambiente de Desenvolvimento](01.md){:target="_blank"}
2. [Introdução ao desenvolvimento WEB](02.md){:target="_blank"}
3. [Estruturando seu Projeto e Criando Rotas CRUD](03.md){:target="_blank"}
4. [Configurando Banco de Dados e Gerenciando Migrações com Alembic](04.md){:target="_blank"}
5. [Integrando Banco de Dados a API](05.md){:target="_blank"}
6. [Autenticação e Autorização](06.md){:target="_blank"}
7. [Refatorando a Estrutura do Projeto](07.md){:target="_blank"}
8. [Tornando o projeto assíncrono](08.md){:target="_blank"}
9. [Tornando o sistema de autenticação robusto](09.md){:target="_blank"}
10. [Criando Rotas CRUD para Tarefas](10.md){:target="_blank"}
11. [Dockerizando a nossa aplicação e introduzindo o PostgreSQL](11.md){:target="_blank"}
12. [Automatizando os testes com integração contínua](12.md){:target="_blank"}
13. [Fazendo o deploy no Fly.io](13.md){:target="_blank"}
14. [Despedida e próximos passos](14.md){:target="_blank"}

Após todas as aulas, se você sentir que ainda quer evoluir mais e testar seus conhecimentos, [temos um projeto final](14.md){:target="_blank"} para avaliar o quanto você aprendeu.

### 🦖 Quem vai ministrar essas aulas?

Prazer! Eu me chamo Eduardo. Mas as pessoas me conhecem na internet como [@dunossauro](https://dunossauro.com){:target="_blank"}.

<div class="sbs" markdown>
![Uma fotografia minha, Dunossauro, sentado em um banco com um por do sol ao fundo](assets/readme/dunossauro.jpg){ align=left width="300" .shadow}
<div markdown>

Sou um programador Python muito empolgado e curioso. Toco um projeto pessoal chamado [Live de Python](https://www.youtube.com/@Dunossauro){:target="_blank"} há quase 7 anos. Onde conversamos sobre tudo e mais um pouco quando o assunto é Python.

Esse projeto que estamos desenvolvendo é um pedaço, um projeto, de um grande curso de FastAPI que estou montando. Espero que você se divirta ao máximo com a parte prática enquanto escrevo em mais detalhes todo o potencial teórico que lançarei no futuro!

[Caso queira saber mais sobre esse projeto completo](https://youtu.be/ikmFLkjxqFg){:target="_blank"}.
</div>
</div>

## :face_with_monocle: Revisão e contribuições

Esse material contou com a revisão e contribuições inestimáveis de pessoas incríveis:

[@adorilson](https://github.com/adorilson){:target="_blank"}, [@aguynaldo](https://github.com/aguynaldo){:target="blank"}, [@alphabraga](https://github.com/alphabraga){:target="_blank"}, [@andrespp](https://github.com/andrespp){:target="_blank"}, [@azmovi](https://github.com/azmovi){:target="_blank"}, [@bugelseif](https://github.com/bugelseif){:target="_blank"}, [@FtxDante](https://github.com/FtxDante){:target="_blank"}, [@gabrielhardcore](https://github.com/gabrielhardcore){:target="_blank"}, [@gbpagano](https://github.com/gbpagano){:target="_blank"}, [@henriqueccda](https://github.com/henriqueccda){:target="_blank"}, [@henriquesebastiao](https://github.com/henriquesebastiao){:target="_blank"}, [@ig0r-ferreira](https://github.com/ig0r-ferreira){:target="_blank"}, [@itsGab](https://github.com/itsGab){:target="_blank"}, [@ivansantiagojr](https://github.com/ivansantiagojr){:target="_blank"}, [@jlplautz](https://github.com/jlplautz){:target="_blank"}, [@jonathanscheibel](https://github.com/jonathanscheibel){:target="_blank"}, [@jpsalviano](https://github.com/jpsalviano){:target="_blank"}, [@julioformiga](https://github.com/julioformiga){:target="_blank"}, [@KennedyRichard](https://github.com/KennedyRichard){:target="_blank"}, [@lbmendes](https://github.com/lbmendes){:target="_blank"}, [@lucasmpavelski](http://github.com/lucasmpavelski){:target="_blank"}, [@lucianoratamero](https://github.com/lucianoratamero){:target="_blank"}, [@matheusalmeida28](https://github.com/matheusalmeida28){:target="_blank"}, [matheussricardoo](https://github.com/matheussricardoo){:target="_blank"}, [@me15degrees](https://github.com/me15degrees){:target="_blank"}, [@mmaachado](https://github.com/mmaachado){:target="_blank"}, [@NatalNW7](https://github.com/NatalNW7){:target="_blank"}, [@raiguilhermems](https://github.com/raiguilhermems){:target="_blank"}, [@rennerocha](https://github.com/rennerocha){:target="_blank"}, [@ricardo-emanuel01](https://github.com/ricardo-emanuel01){:target="_blank"}, [@rodbv](https://github.com/rodbv){:target="_blank"}, [@rodrigosbarretos](https://github.com/rodrigosbarretos){:target="_blank"}, [@taconi](https://github.com/taconi){:target="_blank"}, [@ThiagoEidi](https://github.com/ThiagoEidi){:target="_blank"}, [@wanderleihuttel](https://github.com/wanderleihuttel){:target="_blank"}, [@williangl](https://github.com/williangl){:target="_blank"}, [@vcwild](https://github.com/vcwild){:target="_blank"}, [@vdionysio](https://github.com/vdionysio){:target="_blank"}

{++**Muito obrigado!**++} :heart:

## 📖 Licença

Todo esse curso foi escrito e produzido por Eduardo Mendes ([@dunossauro](https://dunossauro.com/){:target="_blank"}).

Todo esse material é gratuito e está sob licença Creative Commons [BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/){:target="_blank"}. O que significa que:

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
4. Uma conta no [Github](https://github.com/){:target="_blank"}: para podermos testar com Github Actions;
5. Uma conta no [Fly.io](https://fly.io/){:target="_blank"}: ferramenta que usaremos para fazer deploy.

## 🔧 Ferramentas de apoio

Toda essa página foi feita usando as seguintes bibliotecas:

- [MkDocs](https://www.mkdocs.org/){:target="_blank"}: Para geração das páginas estáticas usando Markdown
- [Mkdocs-material](https://squidfunk.github.io/mkdocs-material/){:target="_blank"}: Tema para o MkDocs
- [pymdown-extensions](https://facelessuser.github.io/pymdown-extensions/){:target="_blank"}: Extensões para MkDocs, como emojis, diagramas e blocos estilizados de código
- [Python-Markdown](https://python-markdown.github.io/){:target="_blank"}: Extensão do Python para Markdown
- [Mkdocs-video](https://github.com/soulless-viewer/mkdocs-video){:target="_blank"}: Extensão para o MkDocs exibir os vídeos na página
- [Mermaid.js](https://mermaid-js.github.io/mermaid/){:target="_blank"}: Construção dos diagramas
- [Glaxnimate](https://glaxnimate.mattbas.org/){:target="_blank"}: Pra criar a animação no topo dessa página
- [Lottie-Player](https://github.com/LottieFiles/lottie-player){:target="_blank"}: Pra exibir a animação do Glaxnimate

Para os slides:

- [marp](https://marp.app/){:target="_blank"}: Onde preparei os slides
- [Rose-Pine](https://github.com/rainbowflesh/Rose-Pine-For-Marp){:target="_blank"}: Tema que usei no marp

### 📁 Repositório
O versionamento de tudo está sendo feito no [repositório do curso Github](https://github.com/dunossauro/fastapi-do-zero){:target="_blank"}

### 🚀 Deploy
Os deploys das páginas estáticas geradas pelo MkDocs estão sendo feitos no [Netlify](https://www.netlify.com/){:target="_blank"}

## Conclusão

Neste curso, a intenção é fornecer uma compreensão completa do framework FastAPI, utilizando-o para construir uma aplicação de gerenciamento de tarefas. O aprendizado será focado na prática, e cada conceito será acompanhado por exemplos e exercícios relevantes.

A jornada começará com a configuração do ambiente de desenvolvimento e introdução ao FastAPI. Ao longo das aulas, abordaremos tópicos como autenticação, operações CRUD, testes com pytest e deploy. A ênfase será colocada na aplicação de boas práticas e no entendimento das ferramentas e tecnologias atualizadas, incluindo as versões mais recentes do FastAPI, Pydantic, SQLAlchemy ORM, Python e Alembic.

Este conteúdo foi pensado para auxiliar na compreensão de como criar uma API eficiente e confiável, dando atenção a aspectos importantes como testes e integração com banco de dados.

Nos vemos na primeira aula. ❤

## F.A.Q.

Perguntas frequentes que me fizeram durante os vídeos:

- Que papel de parede é esse? [É uma foto do Liam Wong](https://www.tumblr.com/liamwong){:target="_blank"}
- Qual o tema no shell? Todo o meu tema do Gnome foi customizado com [Gradience](https://gradienceteam.github.io/){:target="_blank"} o tema é [Pretty In Purple](https://www.gnome-look.org/p/2031597){:target="_blank"}
- Qual o tema do seu editor? [Rebecca](https://github.com/vic/rebecca-theme){:target="_blank"}
