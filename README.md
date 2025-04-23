# FastAPI do Zero

O site gerado por esse repositório está disponível em: [fastapidozero.dunossauro.com](https://fastapidozero.dunossauro.com).

> O objetivo final desse curso é que ele também seja disponibilizado em vídeo quando a escrita do material terminar. Nos vemos no youtube em breve!

O objetivo desse projeto é ensinar FastAPI para pessoas que queiram ter o seu primeiro contato com o mesmo. A ideia padrão é construir uma aplicação pequena e simples, mas executando todos os passos até o deploy.

As Aulas estão dividas em:

0. [Apresentação do curso](https://fastapidozero.dunossauro.com/)
1. [Configurando o Ambiente de Desenvolvimento](https://fastapidozero.dunossauro.com/01/)
2. [Introdução ao desenvolvimento WEB](https://fastapidozero.dunossauro.com/02/)
3. [Estruturando seu Projeto e Criando Rotas CRUD](https://fastapidozero.dunossauro.com/03/)
4. [Configurando Banco de Dados e Gerenciando Migrações com Alembic](https://fastapidozero.dunossauro.com/04/)
5. [Integrando Banco de Dados a API](https://fastapidozero.dunossauro.com/05/)
6. [Autenticação e Autorização](https://fastapidozero.dunossauro.com/06/)
7. [Refatorando a Estrutura do Projeto](https://fastapidozero.dunossauro.com/07/)
8. [Tornando o projeto assíncrono](https://fastapidozero.dunossauro.com/08/)
9. [Tornando o sistema de autenticação robusto](https://fastapidozero.dunossauro.com/09/)
10. [Criando Rotas CRUD para Tarefas](https://fastapidozero.dunossauro.com/10/)
11. [Dockerizando a aplicação](https://fastapidozero.dunossauro.com/11/)
12. [Automatizando os testes com integração contínua](https://fastapidozero.dunossauro.com/12/)
13. [Fazendo o deploy no fly.io](https://fastapidozero.dunossauro.com/13/)
14. [Despedida](https://fastapidozero.dunossauro.com/14/)

---

### Caso precise reconstruir o ambiente para as páginas

#### Sobre o ambiente

Todo esse projeto é gerenciado pelo Poetry, a versão usada durante o momento da escrita é `2.1.2`:

```bash
pipx install poetry==2.1.2
pipx inject poetry poetry-plugin-shell
```

A versão usada do python é a versão 3.13.2:

```
pyenv local 3.13.2
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
deploy      Faz o deploy da página em produção
slides      Gera os slides em pdf
slides_html Gera os slides em html (formato usado nas aulas)
pdf         Cria um pdf único de todo o curso (não otimizado ainda)
```

Para executar qualquer comando, basta usar: `task <comando>`, como por exemplo `task serve`.

#### Sobre os slides

Todos os slides foram feitos usando marp. Versão do marp usada: `4.0.3`. O tema `rose-pine` está dentro da pasta dos slides brutos.


## Gerar nova release

> TODO: Deixar isso melhor documentado

- Criar uma release no towncrier
- Criar a tag do git
- Criar uma release no mike na tag e dá push
- Sobe a release com `task deploy`


### Caso a documentação antiga precise ser atualizada (> 4.0)

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
