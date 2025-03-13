# 4.0 (2025-03-13)

## Prontos principais da release

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
