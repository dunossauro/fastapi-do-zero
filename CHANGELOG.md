# 4.0.3 (2025-05-27)

### Adicionado

- Tip para rodar os testcontaners caso esteja usando podman

### Correções

- Diversas correções de texto na aula 01 por [@renan-asantos](https://github.com/renan-asantos) ([#356](https://github.com/dunossauro/fastapi-do-zero/issues/356))
- Diversos typos na aula 03 por [@renan-asantos](https://github.com/renan-asantos) ([#376](https://github.com/dunossauro/fastapi-do-zero/issues/376))
- Correções de typos na aula 08 por [@kylefelipe](https://github.com/kylefelipe) ([#380](https://github.com/dunossauro/fastapi-do-zero/issues/380))
- Remoção de warning na resolução do exercício 04 da aula 10, por [@kylefelipe](https://github.com/kylefelipe) ([#382](https://github.com/dunossauro/fastapi-do-zero/issues/382))
- Ajustando todos os endpoints para usarem Annotated na aula 07

### Alterado

- Adicionando flag para não instalar as dependências de desenvolvimento no container docker. ([#369](https://github.com/dunossauro/fastapi-do-zero/issues/369))
- Coesão e fluidez de texto na aula 04 por [@renan-asantos](https://github.com/renan-asantos) ([#383](https://github.com/dunossauro/fastapi-do-zero/issues/383))
- Links para aulas 01 à 06 atualizadas no cabeçalho do texto
- Playlist de funções como referência dos pré-requisitos

### Atualizações

- `alembic` 1.15.2 -> 1.16.1
- `freezegun` 1.5.1 -> 1.5.2
- `psycopg[binary]` 3.2.7 -> 3.2.9
- `pytest-asyncio` 0.26 -> 1.0.0
- `ruff` 0.11.8 -> 0.11.11
- `sqlalchemy` 2.0.40 -> 2.0.41

### Interno

- Adicionando badge "not by ai" no footer e na página principal ([#357](https://github.com/dunossauro/fastapi-do-zero/issues/357))
- CI rodando somente em alterações de código
- `mkdocs-material` 9.6.12 -> 9.6.14

### Slides

- Correção dos links em `04` ([#283](https://github.com/dunossauro/fastapi-do-zero/issues/283))
- Atualização da aula `06` para v4X ([#283](https://github.com/dunossauro/fastapi-do-zero/issues/283))
- Atualização da aula `05` para v4X ([#283](https://github.com/dunossauro/fastapi-do-zero/issues/283))
- Adequação dos slides `07` para v4 ([#283](https://github.com/dunossauro/fastapi-do-zero/issues/283))
- Correções e expansão dos slides `04`
- Remoção do download de fontes no HTML


# 4.0.2 (2025-05-08)

### Adicionado

- Opção de instalação do poetry shell via pipx

### Correções

- Correção gramatical na página de mudanças, por [@ViniciusSouzaRoque](https://github.com/ViniciusSouzaRoque)
- Typo verões -> versões no template de versões

### Interno

- Redirecionamento para 404 via netlify ([#355](https://github.com/dunossauro/fastapi-do-zero/issues/355))
- Adicionando as playlists nas páginas de aulas por ano
- Criando macro para versão mínima suportada do python
- Listando mais ferramentas de apoio a página inicial

### Slides

- Ajustando links e adicionando configuração do taskipy em `01`
- Correção dos links em `00`


# 4.0.1 (2025-05-06)

## Pontos principais da release

- Atualização das bibliotecas
- Versionamento das páginas do curso via mike
- Atualização dos primeiros slides para apresentação de 2025

### Adicionado

- Lock no apendice C

### Correções

- Todos os links agora contam com target blank, iniciado por [ThiagoEidi](https://github.com/ThiagoEidi) ([#337](https://github.com/dunossauro/fastapi-do-zero/issues/337))
- Links absolutos na versão estável ([#348](https://github.com/dunossauro/fastapi-do-zero/issues/348))
- Corrigindo typos (secutiry -> security), por [@nothiel](https://github.com/nothiel)

### Alterado

- Nota de revisão sobre env files no docker recebeu mais insumos
- Simplificações de texto na página inicial

### Atualizações

- Novas respostas sobre ambiente no F.A.Q.
- `FastAPI` 0.115.11 -> 0.115.12
- `alembic` 1.15.1 -> 1.15.2
- `poetry` 2.1.1 -> 2.1.3
- `psycopg[binary]` 3.2.6 -> 3.2.7
- `pytest-asyncio` 0.25 -> 0.26
- `pytest-cov` 6.0 -> 6.1.1
- `ruff` 0.10.0 -> 0.11.8
- `sqlalchemy` 2.0.39 -> 2.0.40
- `testcontainers` 4.9.2 -> 4.10

### Interno

- Versionamento no material de texto ([#345](https://github.com/dunossauro/fastapi-do-zero/issues/345))
- Remoção do export para pdf das páginas ([#346](https://github.com/dunossauro/fastapi-do-zero/issues/346))
- Macros para tags de redirecionamento correto de slides de códigos para versões 4+ ([#347](https://github.com/dunossauro/fastapi-do-zero/issues/347))
- [quiz] Ao clicar no label do form, agora o id é mapeado corretamente. Por [@EvandroNetoo](https://github.com/EvandroNetoo) ([#352](https://github.com/dunossauro/fastapi-do-zero/issues/352))
- Atualização typos `1.30.2` -> `1.32.0`
- `mkdocs-material` 9.6.8 -> 9.6.12

### Slides

- Revisão `00` para 4.0.1 ([#283](https://github.com/dunossauro/fastapi-do-zero/issues/283))
- Revisão `01` para 4.0.1 ([#283](https://github.com/dunossauro/fastapi-do-zero/issues/283))
- Revisão `02` para 4.0.1 ([#283](https://github.com/dunossauro/fastapi-do-zero/issues/283))
- Revisão `03` para 4.0.1 ([#283](https://github.com/dunossauro/fastapi-do-zero/issues/283))


# 4.0 (2025-03-13)

## Pontos principais da release

- Criação de uma nova aula sobre programação assíncrona (08)
- Remoção do pyenv em detrimento do poetry 2.0
- Material suplementar ao fim das aulas
- Novas questões no quiz
- Ampliação dos textos em diversas aulas
- Diversas novas adições de comentários em blocos
- [Datas para apresentação do curso em 2025](aulas/2025.md)


### Adicionado

- Cenários de testes para o TCC sobre autorização e autenticação ([#281](https://github.com/dunossauro/fastapi-do-zero/issues/281))
- Notas sobre `OperationalError` em todas as resoluções de exercícios de migração (04 e 09) ([#291](https://github.com/dunossauro/fastapi-do-zero/issues/291))
- Material complementar (live de python) ao fim do texto das aulas ([#296](https://github.com/dunossauro/fastapi-do-zero/issues/296))
- **Nova aula**: `Tornando o projeto assíncrono` ([#301](https://github.com/dunossauro/fastapi-do-zero/issues/301))
- Uma nova questão foi adicionadas ao quiz da aula 06 ([#304](https://github.com/dunossauro/fastapi-do-zero/issues/304))
- Novas 4 questões foram adicionadas ao quiz da aula 10 ([#304](https://github.com/dunossauro/fastapi-do-zero/issues/304))
- Novas 3 questões foram adicionadas ao quiz da aula 12 ([#304](https://github.com/dunossauro/fastapi-do-zero/issues/304))
- Novas 3 questões foram adicionadas ao quiz da aula 11 ([#304](https://github.com/dunossauro/fastapi-do-zero/issues/304))
- Novas 5 questões foram adicionadas ao quiz da aula 07 ([#304](https://github.com/dunossauro/fastapi-do-zero/issues/304))
- Adicionando nota para psycopg no windows, testado por [@raiguilhermems](https://github.com/raiguilhermems) ([#310](https://github.com/dunossauro/fastapi-do-zero/issues/310))
- Nota sobre a execução do `Act` no Windows. Contribuição de [@marythealice](https://github.com/marythealice) ([#313](https://github.com/dunossauro/fastapi-do-zero/issues/313))
- Material suplementar (live) sobre Factory-boy ([#315](https://github.com/dunossauro/fastapi-do-zero/issues/315))
- Apêncide C com versões das bibliotecas e ferramentas pinadas para consultas futuras ([#317](https://github.com/dunossauro/fastapi-do-zero/issues/317))
- Gerenciamento de versões do python via poetry ([#319](https://github.com/dunossauro/fastapi-do-zero/issues/319))
- `FAST` ao ruff na aula de refatoração ([#323](https://github.com/dunossauro/fastapi-do-zero/issues/323))
- Diversas adições de texto e comentários expandidos em `Criando Rotas CRUD para Gerenciamento de Tarefas em FastAPI`
- Nota sobre a execução do CI localmente via `Act` no docker e podman
- Nota sobre changelogs no topo da página principal
- Novo exercício na aula `Criando Rotas CRUD para Gerenciamento de Tarefas`
- Texto sobre tarefas em background no apêndice B

### Correções

- Tips na aula 06 em `get_current_user` ([#298](https://github.com/dunossauro/fastapi-do-zero/issues/298))
- Erro no exercicio 09 da aula 06: `current_user` -> `get_current_user`, por [@matheussricardoo](https://github.com/matheussricardoo) ([#299](https://github.com/dunossauro/fastapi-do-zero/issues/299))
- [Aula 06] Correção do status code 409 -> 401. Por [@azmovi](https://github.com/azmovi) ([#327](https://github.com/dunossauro/fastapi-do-zero/issues/327))
- Alterando questão 03 do quiz na aula 04, por [@ThiagoEidi](https://github.com/ThiagoEidi)

### Alterado

- [Aula 10] - Quiz agora com `add_all` ([#312](https://github.com/dunossauro/fastapi-do-zero/issues/312))
- [aula 01] Usando o pacote no estilo `flat` na criação do projeto ([#318](https://github.com/dunossauro/fastapi-do-zero/issues/318))
- Correção dos status codes na aula 09 ([#321](https://github.com/dunossauro/fastapi-do-zero/issues/321))
- Correção dos status codes na aula 05 ([#321](https://github.com/dunossauro/fastapi-do-zero/issues/321))
- Correção dos status codes na aula 06 ([#321](https://github.com/dunossauro/fastapi-do-zero/issues/321))
- Correção dos status codes na aula 07 ([#321](https://github.com/dunossauro/fastapi-do-zero/issues/321))
- `refresh_access_token` agora usa Annotated ([#323](https://github.com/dunossauro/fastapi-do-zero/issues/323))
- [readme] Atualização do tópico "O que você vai aprender" ([#330](https://github.com/dunossauro/fastapi-do-zero/issues/330))
- Alterando aula `Criando Rotas CRUD para Gerenciamento de Tarefas em FastAPI` para async **Não compatível com versão anterior**
- Alterando aula `Dockerizando a nossa aplicação e introduzindo o PostgreSQL` para async **Não compatível com versão anterior**
- Alterando aula `Tornando o sistema de autenticação robusto` para async **Não compatível com versão anterior**
- URL fixa para os changelogs

### Removido

- [aula 10] - Questão do quiz sobre #noqa ([#303](https://github.com/dunossauro/fastapi-do-zero/issues/303))
- Instalação do python via pyenv ([#319](https://github.com/dunossauro/fastapi-do-zero/issues/319))

### Atualizações

- `poetry` 2.0.1 -> 2.1.1 ([#307](https://github.com/dunossauro/fastapi-do-zero/issues/307))
- `factory-boy` 3.3.1 -> 3.3.3
- `psycopg[binary]` 3.2.5 -> 3.2.6
- `pydantic-settings` 2.7.1 -> 2.8.0
- `ruff` 0.9.4 -> 0.10.0
- `sqlalchemy ` 2.0.37 -> 2.0.39
- `alembic` 1.14.1 -> 1.15.1
- `fastapi[standard]` 0.115.9 -> 0.115.11
- `pytest` = 8.3.4 -> 8.3.5
- `testcontainers` 4.9.1 -> 4.9.2

### Interno

- Adicionando `markdown-exec` ao projeto
- Atualização do `mkdocs-material`
- Repositório do curso com `package-mode=false`


# 3.0.0 (2025-02-02)

### Adicionado

- Nota sobre possível erro no exercicio exercício 04 da aula 04 por [@taconi](https://github.com/taconi) ([#279](https://github.com/dunossauro/fastapi-do-zero/issues/279))
- [Windows] Notas para erro de Policies na instalação do `pyenv` no guia de instalação ([#284](https://github.com/dunossauro/fastapi-do-zero/issues/284))
- Notas sobre `OAuth2PasswordRequestForm` na aula 06 por [KennedyRichard](https://github.com/KennedyRichard) ([#285](https://github.com/dunossauro/fastapi-do-zero/issues/285))

### Correções

- Integridade conceitual em testes de dicionários ([#286](https://github.com/dunossauro/fastapi-do-zero/issues/286))
- Texto sobre a instalação do `poetry` + `poetry-plugins-shell` na aula 01

### Alterado

- Alterando a máquina padrão do deploy para 512MB de memória por conta das novas atualizações do fly.io ([#288](https://github.com/dunossauro/fastapi-do-zero/issues/288))
- Revisitando o Exercício 01 da aula 02 para ficar mais explícito.

### Removido

- `TokenData` da aulas 06 e 08, para simplificar o fluxo JWT e causar menos confusão ([#290](https://github.com/dunossauro/fastapi-do-zero/issues/290))

### Atualizações

- FastAPI para versão 0.115.8 ([#282](https://github.com/dunossauro/fastapi-do-zero/issues/282))
- Alembic para versão 1.14.1
- Ruff para versão 0.9.4
- testecontainers para versão 4.9.1

### Interno

- Atualização do `mkdocs-material`
- Atualização do `typos`

### Slides

- Revisão dos slides da aula 01 para conformidade com o texto
