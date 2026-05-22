---
title: FastAPI do Zero!
description: Boas vindas ao nosso minicurso de FastAPI!
---

<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
<lottie-player src="https://raw.githubusercontent.com/dunossauro/fastapi-do-zero/main/stuff/anim_lottie.json" background="transparent" speed="1" style="margin-left: auto; margin-right: auto;" loop autoplay></lottie-player>


<div class="flex">
<h1>FastAPI do ZERO</h1>
<img alt="" src="assets/Written-By-Human-Not-By-AI-Badge-white.svg"/>

</div>

{%set aula = "00" %}
{%set link = "ImhYlISeWPQ" %}

??? tip "Caso prefira ver a apresentação do curso em vídeo"
	Esse aula ainda não está disponível em formato de vídeo, somente em texto ou live!
	![type:video](https://www.youtube.com/embed/{{link}})

	[Aula :fontawesome-brands-youtube:](https://youtu.be/{{link}}?list=PLOQgLBuj2-3IuFbt-wJw2p2NiV9WTRzIP){ .md-button }
	[Slides :fontawesome-solid-file-powerpoint:]({{page.canonical_url}}slides/aula_{{aula}}.html){ .md-button }

> Esse material passa por atualizações periódicas. Você pode acompanhar as notas de alterações [aqui](alteracoes.md){:target="_blank"}.

Olá, boas-vindas ao curso de FastAPI!

A nossa intenção neste curso é facilitar o aprendizado no desenvolvimento de APIs usando o FastAPI. Vamos explorar como integrar bancos de dados, criar testes e um sistema básico de autenticação com JWT. Tudo isso para oferecer uma boa base para quem quer trabalhar com desenvolvimento web com Python. A ideia desse curso é apresentar os conceitos de forma prática, construindo um projeto do zero e indo até a sua fase de produção.


## O que é FastAPI?

[FastAPI](https://fastapi.tiangolo.com/){:target="_blank"} é um framework Python moderno, projetado para simplicidade, velocidade e eficiência. A combinação de diversas funcionalidades modernas do Python, como anotações de tipo e suporte à concorrência. Simplificando o desenvolvimento de APIs.


## Sobre o curso

Este curso foi desenvolvido para oferecer uma experiência prática no uso do FastAPI. O objetivo é que você obtenha uma compreensão das funcionalidades do FastAPI e de boas práticas associadas a ele.

O projeto central do curso será a construção de um gerenciador de tarefas (uma lista de tarefas), começando do zero. Esse projeto incluirá a implementação da autenticação do usuário e das operações CRUD completas.

```python exec="1"
import tomllib
from datetime import date

year = date.today().year

with open("codigo_das_aulas/13/poetry.lock", "rb") as f:
    packages = {pkg["name"]: pkg["version"] for pkg in tomllib.load(f)["package"]}

print(
    f"Para a construção do projeto, serão utilizadas as versões mais recentes das ferramentas, disponíveis em {year}, como a versão do {packages['fastapi']} FastAPI, "
    f"a versão {packages['pydantic']} do Pydantic, a versão {packages['sqlalchemy']} do SQLAlchemy ORM, "
    f"além do suporte ao Python 3.11/3.12/3.13/3.14, e do Alembic {packages['alembic']} para gerenciamento de migrações."
)
```

Além da construção do projeto, o curso também incluirá a prática de testes, utilizando o pytest. Essa abordagem planeja garantir que as APIs desenvolvidas sejam não somente funcionais, mas também robustas e confiáveis.

## O que você vai aprender?

Aqui está uma visão geral dos tópicos que abordaremos neste curso:

1. **Configuração do ambiente e gerenciamento de um projeto Python**: começaremos do zero, configurando o ambiente de desenvolvimento. Escolheremos ferramentas adequadas, aplicaremos boas práticas na construção de projetos e integraremos um gerenciador de projetos, task manager, ferramentas de análise estática e formatação de código.

2. **Primeiros Passos com FastAPI**: introduziremos os conceitos do desenvolvimento web com FastAPI, ensinando como criar endpoints, realizar operações CRUD, aplicar injeção de dependência, criar schemas e outros fundamentos.

3. **Modelagem de Dados com Pydantic, SQLAlchemy e Alembic**: aprenderemos a criar e manipular modelos de dados utilizando Pydantic e SQLAlchemy, além de configurar um esquema de migrações de banco de dados utilizando Alembic.

4. **Programação Assíncrona**: a partir da metade do curso, focaremos em tornar nosso projeto totalmente assíncrono, aproveitando os recursos do FastAPI e do SQLAlchemy para operações mais eficientes e escaláveis.

5. **Autenticação e Autorização em FastAPI**: construiremos um sistema completo de autenticação para proteger nossas rotas e garantir que apenas usuários autenticados tenham acesso a dados e funcionalidades específicas.

6. **Foco em testes**: faremos uma introdução detalhada ao desenvolvimento orientado a testes, utilizando pytest e coverage, e aprenderemos a configurar um pipeline de integração contínua com GitHub Actions para garantir a qualidade do código.

7. **Conteinerizando e Fazendo Deploy de sua Aplicação FastAPI**: por fim, aprenderemos a criar um container Docker para nossa aplicação FastAPI e realizaremos o deploy utilizando Fly.io, preparando a aplicação para produção.


## 💰 Esse curso é gratuito?

SIM! Esse curso foi todo desenvolvido [de forma aberta](#licenca){:target="_blank"} e com a [ajuda financeira](https://apoia.se/fastapi){:target="_blank"} de pessoas incríveis. Caso você sinta vontade de contribuir, você pode me pagar um café por pix (pix.dunossauro@gmail.com) ou apoiar a [campanha recorrente de financiamento coletivo da live de python](https://apoia.se/livedepython){:target="_blank"} que é o que paga as contas aqui de casa.

## Onde o curso será disponibilizado?

Esse material será disponibilizado em duas formas diferentes:

1. Em livro texto: todo o material está disponível nessa página;
2. Em aulas síncronas ao vivo: para quem prefere o compromisso de acompanhar em grupo.
    - Playlist das apresentações de 2025:
		<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?si=bbzMgz9dXoVXNdlR&amp;list=PLOQgLBuj2-3KT9ZWvPmaGFQ0KjIez0403" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

		Referente a versão [4.1](/4.1) do texto

	- Playlist das apresentações de 2024:
		<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?si=bbzMgz9dXoVXNdlR&amp;list=PLOQgLBuj2-3IuFbt-wJw2p2NiV9WTRzIP" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

		Referente a versão [1.0](/1.0) do texto

## Pré-requisitos

Para aproveitar ao máximo este curso, é recomendado que você já tenha algum conhecimento prévio em python. Se pudesse listar o que considero importante para não se perder, os tópicos em python importantes são:

- O funcionamento de funções: como criar e usar ([referência](https://www.youtube.com/playlist?list=PLOQgLBuj2-3LqssmOySRIAr5JFoVH7DK0){:target="_blank"});
- O funcionamento das estruturas de dados: como listas, dicionários, etc.;
- Uma pitada sobre objetos: saber o que são métodos e atributos ([referência](https://youtu.be/BALM_oJcJL4){:target="_blank"});
- Classes de dados: o funcionamento básico das dataclasses ([referência](https://youtu.be/NtZY3AmsBSk){:target="_blank"}).

> As referências servem como base caso você ainda não tenha estudado esses assuntos.

Alguns outros tópicos não relativos a python também serão abordados. Então, é interessante que você tenha algum entendimento básico sobre:


- Desenvolvimento Web e APIs RESTful: não essencial, pois iremos abordar, mas quanto mais você souber, melhor para acompanhar.
- Banco de dados / SQL: Um conhecimento básico sobre criação e busca de dados usando SQL já é suficiente, embora esse tópico também seja como o anterior, quanto mais você souber, melhor.
- Git: não nos aprofundaremos nesse tópico durante o curso, mas usaremos operações elementares de git (como commit e push).
- Docker: também não nos aprofundaremos nesse tópico e ele só será abordado nas aulas finais. Mas, também, só usaremos comandos básicos de docker e docker-compose.

??? info "Caso esteja iniciando seus estudos em Python!"
	Caso você ainda não se sinta uma pessoa preparada, ou caiu aqui sem saber exatamente o que esperar. Temos um pequeno curso introdutório. Destinado aos primeiros passos com python.
	![type:video](https://youtube.com/embed/yTQDbqmv8Ho)

	[:fontawesome-brands-youtube: Link direto](https://www.youtube.com/watch?v=yTQDbqmv8Ho){ .md-button }

	Também temos uma live focada em dicas para iniciar os estudos em python

    ![type:video](https://www.youtube.com/embed/HSotf1Amess)

	[:fontawesome-brands-youtube: Link direto](https://www.youtube.com/watch?v=HSotf1Amess){ .md-button }

	Ou então a leitura do livro [**Pense em python**](https://penseallen.github.io/PensePython2e/){:target="_blank"}

## Aulas

1. [Configurando o ambiente de desenvolvimento](01.md){:target="_blank"}
2. [Introdução ao desenvolvimento WEB](02.md){:target="_blank"}
3. [Estruturando seu projeto e criando rotas CRUD](03.md){:target="_blank"}
4. [Configurando o banco de dados e gerenciando migrações com Alembic](04.md){:target="_blank"}
5. [Integrando o banco de dados à API](05.md){:target="_blank"}
6. [Autenticação e Autorização com JWT](06.md){:target="_blank"}
7. [Refatorando a estrutura do projeto](07.md){:target="_blank"}
8. [Tornando o projeto assíncrono](08.md){:target="_blank"}
9. [Tornando o sistema de autenticação robusto](09.md){:target="_blank"}
10. [Criando rotas CRUD para gerenciamento de tarefas](10.md){:target="_blank"}
11. [Dockerizando a nossa aplicação e introduzindo o PostgreSQL](11.md){:target="_blank"}
12. [Automatizando os testes com integração contínua](12.md){:target="_blank"}
13. [Fazendo o deploy no Fly.io](13.md){:target="_blank"}
14. [Despedida e próximos passos](14.md){:target="_blank"}

Após todas as aulas, se você sentir que ainda quer evoluir mais e testar seus conhecimentos, [temos um projeto final](15.md){:target="_blank"} para avaliar o quanto você aprendeu.

### 🦖 Quem vai ministrar essas aulas?

Prazer! Eu me chamo Eduardo. As pessoas me conhecem na internet como [@dunossauro](https://dunossauro.com){:target="_blank"}.

<div class="sbs" markdown>
![Uma fotografia minha, Dunossauro, sentado em um banco com um por do sol ao fundo](assets/readme/dunossauro.jpg){ align=left width="300" .shadow}
<div markdown>

Sou um programador Python muito apaixonado e curioso. Toco um projeto pessoal semanal chamado [Live de Python](https://www.youtube.com/@Dunossauro){:target="_blank"} há pouco mais de 8 anos. Onde conversamos sobre tudo e mais um pouco quando o assunto é Python.

Adoro escrever (estamos aqui, não é mesmo?), programar coisas malucas, fazer música com programação e papear sobre software livre, computabilidade e IndieWeb.

Tô sempre pela web e nos eventos de Python, a gente pode se conectar nessa imensa rede mundial de computadores. [Meus links!](https://dunossauro.com){:target="_blank"}.
</div>
</div>

## :face_with_monocle: Revisão e contribuições

Esse material contou com a revisão e contribuições inestimáveis de pessoas incríveis:

[@0xluc](https://github.com/0xluc){:target="_blank"},
[@adorilson](https://github.com/adorilson){:target="_blank"},
[@aguynaldo](https://github.com/aguynaldo){:target="blank"},
[@alphabraga](https://github.com/alphabraga){:target="_blank"},
[@andrespp](https://github.com/andrespp){:target="_blank"},
[@azmovi](https://github.com/azmovi){:target="_blank"},
[@bugelseif](https://github.com/bugelseif){:target="_blank"},
[@dias-gxstavo](https://github.com/dias-gxstavo){:target="_blank"},
[@EvandroNetoo](https://github.com/EvandroNetoo){:target="_blank"},
[@Felipe-Paschoal](https://github.com/Felipe-Paschoal){:target="_blank"},
[@FtxDante](https://github.com/FtxDante){:target="_blank"},
[@gabrielhardcore](https://github.com/gabrielhardcore){:target="_blank"},
[@gbpagano](https://github.com/gbpagano){:target="_blank"},
[@henriqueccda](https://github.com/henriqueccda){:target="_blank"},
[@henriquesebastiao](https://github.com/henriquesebastiao){:target="_blank"},
[@ig0r-ferreira](https://github.com/ig0r-ferreira){:target="_blank"},
[@itsGab](https://github.com/itsGab){:target="_blank"},
[@ivansantiagojr](https://github.com/ivansantiagojr){:target="_blank"},
[jaugustorufino](https://github.com/jaugustorufino){:target="_blank"},
[@jlplautz](https://github.com/jlplautz){:target="_blank"},
[@jonathanscheibel](https://github.com/jonathanscheibel){:target="_blank"},
[@jpsalviano](https://github.com/jpsalviano){:target="_blank"},
[@julioformiga](https://github.com/julioformiga){:target="_blank"},
[@kylefelipe](https://github.com/kylefelipe){:target="_blank"},
[@KennedyRichard](https://github.com/KennedyRichard){:target="_blank"},
[@lbmendes](https://github.com/lbmendes){:target="_blank"},
[@lucasmpavelski](http://github.com/lucasmpavelski){:target="_blank"},
[@lucianoratamero](https://github.com/lucianoratamero){:target="_blank"},
[@luciormoraes](https://github.com/luciormoraes){:target="_blank"},
[@marythealice](https://github.com/marythealice){:target="_blank"},
[@matheusalmeida28](https://github.com/matheusalmeida28){:target="_blank"},
[matheussricardoo](https://github.com/matheussricardoo){:target="_blank"},
[@me15degrees](https://github.com/me15degrees){:target="_blank"},
[@mmaachado](https://github.com/mmaachado){:target="_blank"},
[@NatalNW7](https://github.com/NatalNW7){:target="_blank"},
[@raiguilhermems](https://github.com/raiguilhermems){:target="_blank"},
[@renan-asantos](https://github.com/renan-asantos){:target="_blank"},
[@rennerocha](https://github.com/rennerocha){:target="_blank"},
[@ricardo-emanuel01](https://github.com/ricardo-emanuel01){:target="_blank"},
[@rodbv](https://github.com/rodbv){:target="_blank"},
[@rodrigosbarretos](https://github.com/rodrigosbarretos){:target="_blank"},
[@taconi](https://github.com/taconi){:target="_blank"},
[@thiagonebuloni](https://github.com/thiagonebuloni){:target="_blank"},
[@ThiagoEidi](https://github.com/ThiagoEidi){:target="_blank"},
[@wanderleihuttel](https://github.com/wanderleihuttel){:target="_blank"},
[@williangl](https://github.com/williangl){:target="_blank"},
[@vcwild](https://github.com/vcwild){:target="_blank"},
[@vdionysio](https://github.com/vdionysio){:target="_blank"},
[@ViniciusSouzaRoque](https://github.com/ViniciusSouzaRoque){:target="_blank"}

{++**Muito obrigado!**++} :heart:

Caso tenha interesse em contribuir também, você pode ler o [guia de contribuição](contribua/contribua.md).

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
3. Ter o interpretador Python instalado em uma versão [oficialmente suportada](https://devguide.python.org/versions/){:target="_blank"}, atualmente {{python_supported_version}}+.
4. Uma conta no [Github](https://github.com/){:target="_blank"}: para podermos testar com Github Actions;
5. Uma conta no [Fly.io](https://fly.io/){:target="_blank"}: ferramenta que usaremos para fazer deploy.

## Conclusão

Neste curso, a intenção é fornecer uma compreensão completa do framework FastAPI, utilizando-o para construir uma aplicação de gerenciamento de tarefas. O aprendizado será focado na prática, e cada conceito será acompanhado por exemplos e exercícios relevantes.

A jornada começará com a configuração do ambiente de desenvolvimento e introdução ao FastAPI. Ao longo das aulas, abordaremos tópicos como autenticação, operações CRUD, testes com pytest e deploy. A ênfase será colocada na aplicação de boas práticas e no entendimento das ferramentas e tecnologias atualizadas, incluindo as versões mais recentes do FastAPI, Pydantic, SQLAlchemy ORM, Python e Alembic.

Este conteúdo foi pensado para auxiliar na compreensão de como criar uma API eficiente e confiável, dando atenção a aspectos importantes como testes e integração com banco de dados.

Nos vemos na primeira aula. ❤

---

## 🔧 Ferramentas de apoio

Todo o conteúdo deste material foi produzido **intencionalmente** com ferramentas [FLOSS](https://pt.wikipedia.org/wiki/Software_livre_e_de_c%C3%B3digo_aberto){:target="_blank"}.

### 📝 Para a página

Toda essa página foi escrita em markdown usando as seguintes bibliotecas:

- [MkDocs](https://www.mkdocs.org/){:target="_blank"}: Para geração das páginas estáticas usando Markdown
- [Mkdocs-material](https://squidfunk.github.io/mkdocs-material/){:target="_blank"}: Tema para o MkDocs
- [Pymdown-extensions](https://facelessuser.github.io/pymdown-extensions/){:target="_blank"}: Extensões para MkDocs, como emojis, diagramas e blocos estilizados de código
- [Markdown-exec](https://pawamoy.github.io/markdown-exec/){:target="_blank"}: Utilitários para executar snippets dinâmicos de código e adicionar o resultado em markdown
- [Python-Markdown](https://python-markdown.github.io/){:target="_blank"}: Extensão do Python para Markdown
- [Mkdocs-video](https://github.com/soulless-viewer/mkdocs-video){:target="_blank"}: Extensão para o MkDocs exibir os vídeos na página
- [mkdocs-towncrier](https://github.com/davfsa/mkdocs-towncrier){:target="_blank"}: Extensão para exibir os changelogs do [towncrier](https://towncrier.readthedocs.io/en/stable/index.html) no mkdocs
- [Mkdocs-quiz](https://github.com/skyface753/mkdocs-quiz){:target="_blank"}: Para os questionários sobre as aulas
- [mkdocs-video](https://github.com/soulless-viewer/mkdocs-video){:target="_blank"}: Para exibir os vídeos do youtube nas páginas
- [mkdocs-macros](https://mkdocs-macros-plugin.readthedocs.io/en/latest/){:target="_blank"}: Para criação de macros e variações de textos usando variáveis
- [mike](https://github.com/jimporter/mike){:target="_blank"}: Para manter múltiplas versões do mkdocs online

Ferramentas que não fazem parte do ecossistema markdown, mas se misturam:

- [jinja2](https://jinja.palletsprojects.com/en/stable/){:target="_blank"}: Para escrever blocos reutilizáveis
- [Mermaid.js](https://mermaid-js.github.io/mermaid/){:target="_blank"}: Construção dos diagramas
- [Glaxnimate](https://glaxnimate.mattbas.org/){:target="_blank"}: Para criar a animação no topo dessa página
- [Lottie-Player](https://github.com/LottieFiles/lottie-player){:target="_blank"}: Para exibir a animação do Glaxnimate

### 💬 Para os slides

Tudo também feito com markdown, usando:

- [marp](https://marp.app/){:target="_blank"}: Onde preparei os slides
- [Rose-Pine](https://github.com/rainbowflesh/Rose-Pine-For-Marp){:target="_blank"}: Tema que usei no marp

### 📺 Para as transmissões

Foi utilizado o [Open Broadcaster Software (OBS)](https://obsproject.com/){:target="_blank"}.

### 🖼️ Thumbnails para YouTube

Para tratamento das imagens foi usado o [Darktable](https://www.darktable.org/){:target="_blank"}, para a composição das thumbnails foi usado o [Inkscape](https://inkscape.org/){:target="_blank"}.

### 📁 Repositório

O versionamento de tudo está sendo feito pelo [git](https://git-scm.com/){:target="_blank"} e está disponível no [repositório do curso Github](https://github.com/dunossauro/fastapi-do-zero){:target="_blank"}.

### 🚀 Deploy

Os deploys das páginas estáticas geradas pelo MkDocs estão sendo feitos no [Netlify](https://www.netlify.com/){:target="_blank"}

## ❓ F.A.Q.

Perguntas frequentes não técnicas que me fizeram durante as aulas:

- Que papel de parede é esse? [É uma foto do Liam Wong](https://www.tumblr.com/liamwong){:target="_blank"}.
- Qual sistema operacional está usando? Eu uso GNU/Linux, a distribuição é o [EndeavourOS](https://endeavouros.com/){:target="_blank"}.
- Qual terminal está usando? O [Terminator](https://gnome-terminator.org/){:target="_blank"}.
- Qual editor de texto está usando? O [GNU/Emacs](https://www.gnu.org/software/emacs/){:target="_blank"}.
- Qual o tema que está suando no sistema? O [Catppuccin Mocha](https://catppuccin.com/){:target="_blank"}. Eu uso ele no shell e no editor de texto.
- Onde estão suas configurações do sistema? Em [https://dunossauro.com/dotfiles](https://dunossauro.com/dotfiles){:target="_blank"}.
