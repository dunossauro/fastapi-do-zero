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

## Bumb das dependências usadas em aula

```bash
poetry run invoke update-sub
```

Esse comando vai iterar entre todos os diretórios de `codigo_das_aulas` e vai atualizar as dependências usadas.
