# Como fazer?

Esta página é destinada a algumas coisas bastante específicas para contribuir no projeto. Algumas são uma mera lembrança para mim mesmo de como fazer, outras para futuras contribuições.

> Caso precise de instruções rápidas para contribuição, pode ler o [Guia de contribuição](/contribua/contribua/).

## Bumb de dependências

Rotineiramente, as dependências usadas tanto no projeto que gera esse site quanto as dependências do código das aulas precisam ser atualizadas.

Na raiz do projeto temos um arquivo de tasks do [invoke](https://www.pyinvoke.org/) o `tasks.py`:

```bash
poetry run invoke --list
Available tasks:

  command-sub
  lint-sub
  test-act
  test-compose
  test-docker-build
  test-migrations
  test-sub
  typos-sub
  update-project
  update-sub
  win-test-last-class
  win-test-migration
```

Quase todas essas tarefas são destinadas ao CI, por conta das peculiaridades de rodar em 13 subdiretórios. Duas são referentes ao bump: `update-project` e `typos-sub`.

> No passado, eu fazia isso via poetry-plugin-up, que ficou sem funcionar durante a atualização para a versão 2+ do poetry. Isso foi corrigido, portanto, pode ser que facilite bastante as tasks no futuro.

## Bumb do projeto da página

```bash
poetry run invoke update-project
```

Esse comando vai atualizar as dependências usadas pelo mkdocs da página.

Caso alguma alteração seja algo que impacte a página ou seja uma mudança radical durante essa alteração. É importante gerar um changelog para `interno`:

```bash
poetry run towncrier create
Issue number (`+` if none): +
Fragment type (adicionado, correcoes, alterado, removido, atualizacoes, {++interno++}, slides):
```


## Bumb das dependências usadas em aula

```bash
poetry run invoke update-sub
```

Esse comando vai iterar entre todos os diretórios de `codigo_das_aulas` e vai atualizar as dependências usadas.


Isso pode resultar em atualizações de dois grupos de dependências:

1. Dependências diretas do projeto: FastAPI, SQLAlchemy, ruff ...
2. Dependências indiretas: Starlette, faker, ...

Caso exista alguma alteração no primeiro grupo, deve ser gerado um changelog dela com `atualizacoes`.

Para ver se alguma dependência direta foi atualizada?

```bash
git diff codigo_das_aulas/13/pyproject.toml
```

Se algo foi alterado nesse arquivo, deve ser gerado um changelog. Mas, antes, veja se já não existe um fragmento para ele. Por exemplo, uma nova atualização do fastapi:

```bash
grep -H "fastapi" changelogs/*
changelogs/+52b01b9d.atualizacoes.md:`fastapi` 0.120 -> 0.134
```

Isso quer dizer que já existe um fragmento. Caso não exista, neste caso, crie um novo.

Caso a atualização seja de uma dependência indireta, isso não deve gerar um changelog.
