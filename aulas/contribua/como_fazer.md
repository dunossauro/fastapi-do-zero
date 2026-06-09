# Como fazer?

Esta página é destinada a algumas coisas bastante específicas para contribuir no projeto. Algumas são uma mera lembrança para mim mesmo de como fazer, outras para futuras contribuições.

> Caso precise de instruções rápidas para contribuição, pode ler o [Guia de contribuição](/contribua/contribua/).

## Bumb de dependências

Rotineiramente, as dependências usadas tanto no projeto que gera esse site quanto as dependências do código das aulas precisam ser atualizadas.

Forma simples: Usar as tasks do [taskpy](https://github.com/taskipy/taskipy) que estão no pyproject:

```bash
poetry run task --list
# ... outras resposta
bump         Atualiza todas as dependências do projeto
bump_classes Atualiza todas as dependências das aulas
```

Forma mais complicada: na raiz do projeto temos um arquivo de tasks do [invoke](https://www.pyinvoke.org/) o `tasks.py`:

```bash
poetry run invoke --list
Available tasks:
  
  # outras respostas:
  update-sub
  win-test-last-class
  win-test-migration
```

O `update-sub` é referente à atualização das dependências no código das aulas. Você pode chamá-lo diretamente pelo taskipy, ou chamá-lo pelo invoke:

```bash
poetry run invoke update-sub
```

> No passado, eu fazia isso via poetry-plugin-up, que ficou sem funcionar durante a atualização para a versão 2+ do poetry. Isso foi corrigido, portanto, pode ser que facilite bastante as tasks no futuro.

## Bumb do projeto da página

```bash
poetry run task bump
```

Esse comando vai atualizar as dependências usadas pelo mkdocs da página.

Caso alguma alteração seja algo que impacte a página ou uma mudança radical durante essa alteração. É importante gerar um changelog para `interno`:

```bash
poetry run towncrier create
Issue number (`+` if none): +
Fragment type (adicionado, correcoes, alterado, removido, atualizacoes, {++interno++}, slides):
```


## Bumb das dependências usadas em aula

```bash
poetry run task bump_classes
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

Isso quer dizer que já existe um fragmento. Caso não exista, neste caso, crie um novo fragmento de `atualizacoes`:

```bash
poetry run towncrier create
Issue number (`+` if none): +
Fragment type (adicionado, correcoes, alterado, removido, {++atualizacoes++}, interno, slides):
```

Caso a atualização seja de uma dependência indireta, isso não deve gerar um changelog.

## Reconstruir o ambiente


Caso precise reconstruir o ambiente para as páginas

### Sobre o ambiente

Todo esse projeto é gerenciado pelo Poetry, a versão usada durante o momento da escrita é `2.3`:

```bash
pipx install poetry==2.3
pipx inject poetry poetry-plugin-shell
pipx inject poetry poetry-plugin-up
```

A versão usada do python é a versão 3.13:

```
poetry python install 3.13
```

para configurar todo o ambiente, basta executar:

```bash
poetry install
```

para ativar o ambiente virtual:

```bash
poetry shell
```

### Sobre os comandos

Os comandos para executar funções como deploy, servidor local, geração de slides, etc. estão todos sendo feitos com o [taskipy](https://github.com/taskipy/taskipy):

```bash
task --list
serve       Executa o servidor local do mkdocs
mserve      Executa o servidor local do mkdocs via mike
deploy      Faz o deploy da página em produção usando mike
slides      Gera os slides em html
ruff        ruff check
```

Para executar qualquer comando, basta usar: `task <comando>`, como, por exemplo, `task serve`.

#### Sobre os slides

Todos os slides foram feitos usando [marp](https://marp.app/). Versão do marp usada: `4.2`. O tema `rose-pine`, com algumas modificações, está na pasta dos slides brutos.


## Passos para gerar nova release

### 1. Fazer o build dos changelogs

`towncrier build --version <versao>`, algo como:

```bash
towncrier build --version 4.0.2
```

### 2. Atualizar o pyproject

A versão deve ser atualizada no campo `project.version`:

```toml
[project]
name = "fastapi-do-zero"
version = "4.0.2"
```

### 3. Atualizar tag `current_version` no mkdocs

```yaml
# ... mkdocs.yml
extra:
  current_tag: v4.0.2 # para tag
```

### 4. Fazer o commit

```bash
git add .
git commit -m "Upadate para v4.0.2"
```

### 5. Criar a tag do git

```bash
git tag v4.0.2
git push --tags
```

### 6. Criar versão do mike

> TODO: Isso só vale para majors

### 7. Fazer o deploy atualizado

```bash
mike deploy --push 4.0  # atualizar a versão
```

#### Caso a documentação antiga precise ser atualizada (> 4.0)

O `mike` foi introduzido após a v4.0. Você precisa aplicar o diff abaixo, caso precise atualizar algo:

<details>

<summary> Diff que precisa ser aplicado antes!</summary>

```diff
diff --git a/mkdocs.yml b/mkdocs.yml
index 38c5b9f..7ed5c54 100644
--- a/mkdocs.yml
+++ b/mkdocs.yml
@@ -67,14 +67,6 @@ plugins:
       show_line_count: true
   - git-revision-date-localized
   - social
-  - with-pdf:
-      author: Eduardo Mendes (@dunossauro)
-      cover_title: FastAPI do zero
-      cover_subtitle: Uma introdução prática!
-      copyright: CC BY-NC-SA
-      toc_level: 6
-      enabled_if_env: ENABLE_PDF_EXPORT
-      toc_title: Índice
   - exclude:
       glob:
         - "wip.md"
@@ -115,6 +107,8 @@ extra:
       link: https://dunossauro.com
     - icon: simple/codeberg
       link: https://codeberg.org/dunossauro
+  version:
+    provider: mike

 hooks:
   - hooks/quiz_hook.py
```

</details>

Exemplo do comando do mike:

```bash
mike deploy --push 4.0 --allow-empty
# onde 4.0 é a versão da tag da documentação
```
