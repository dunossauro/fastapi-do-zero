# FastAPI do Zero

O site gerado por esse repositório está disponível em: [fastapidozero.dunossauro.com](https://fastapidozero.dunossauro.com).

O objetivo desse projeto é ensinar FastAPI para pessoas que queiram ter o seu primeiro contato com o mesmo. A ideia padrão é construir uma aplicação pequena e simples, mas executando todos os passos até o deploy.

As Aulas estão dividas em:

0. [Apresentação do curso](https://fastapidozero.dunossauro.com/)
1. [Configurando o ambiente de desenvolvimento](https://fastapidozero.dunossauro.com/estavel/01/)
2. [Introdução ao desenvolvimento WEB](https://fastapidozero.dunossauro.com/estavel/02/)
3. [Estruturando o projeto e criando rotas CRUD](https://fastapidozero.dunossauro.com/estavel/03/)
4. [Configurando banco de dados e gerenciando migrações com Alembic](https://fastapidozero.dunossauro.com/estavel/04/)
5. [Integrando banco de dados à API](https://fastapidozero.dunossauro.com/estavel/05/)
6. [Autenticação e Autorização com JWT](https://fastapidozero.dunossauro.com/estavel/06/)
7. [Refatorando a estrutura do projeto](https://fastapidozero.dunossauro.com/estavel/07/)
8. [Tornando o projeto assíncrono](https://fastapidozero.dunossauro.com/estavel/08/)
9. [Tornando o sistema de autenticação robusto](https://fastapidozero.dunossauro.com/estavel/09/)
10. [Criando Rotas CRUD para gerenciamento de tarefas](https://fastapidozero.dunossauro.com/estavel/10/)
11. [Dockerizando a aplicação](https://fastapidozero.dunossauro.com/estavel/11/)
12. [Automatizando os testes com integração contínua](https://fastapidozero.dunossauro.com/estavel/12/)
13. [Fazendo o deploy no fly.io](https://fastapidozero.dunossauro.com/estavel/13/)
14. [Despedida](https://fastapidozero.dunossauro.com/estavel/14/)

Após todas as aulas, se você sentir que ainda quer evoluir mais e testar seus conhecimentos, [temos
um projeto final](https://fastapidozero.dunossauro.com/estavel/15/) para avaliar o quanto você aprendeu.

---

### Caso precise reconstruir o ambiente para as páginas

#### Sobre o ambiente

Todo esse projeto é gerenciado pelo Poetry, a versão usada durante o momento da escrita é `2.1.3`:

```bash
pipx install poetry==2.2
pipx inject poetry poetry-plugin-shell
```

A versão usada do python é a versão 3.13.2:

```
poetry python install 3.13
```

para configurar todo o ambiente basta executar:

```bash
poetry install
```

para ativar o ambiente virtual:

```bash
poetry shell
```

#### Sobre os comandos

Os comandos para executar funções como deploy, servidor local, geração de slides, etc. Estão todas sendo feitas pelo `taskipy`:

```bash
task --list
serve       Executa o servidor local do mkdocs
mserve      Executa o servidor local do mkdocs via mike
deploy      Faz o deploy da página em produção usando mike
slides      Gera os slides em html
ruff        ruff check
```

Para executar qualquer comando, basta usar: `task <comando>`, como por exemplo `task serve`.

#### Sobre os slides

Todos os slides foram feitos usando marp. Versão do marp usada: `4.0.3`. O tema `rose-pine`, com algumas modificações, está dentro da pasta dos slides brutos.


## Passos para gerar nova release

> TODO: Deixar isso melhor documentado

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
