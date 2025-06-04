---
marp: true
theme: rose-pine
style: |
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
---

# 01 - Configurando o Ambiente de Desenvolvimento

> https://fastapidozero.dunossauro.com/4.0/01/

---

# Objetivos dessa aula:

- Introdução ao ambiente de desenvolvimento
    - ferramentas, testes, configuração, etc
- Instalação do FastAPI e suas dependências
- Configuração das ferramentas de desenvolvimento
- Execução do primeiro "Hello, World!" com FastAPI com testes!

---

# O ambiente de desenvolvimento

1. Um editor de texto a sua escolha (Eu vou usar o [GNU/Emacs](https://www.gnu.org/software/emacs/))
   - Kate, vim, emacs, vscodium, ...
2. Um terminal a sua escolha (Usarei o [Terminator](https://gnome-terminator.org/))
   - Ghostty, tilix, iTerm2, windows terminal (WSL/Powershell)
3. Uma versão [suportada](https://devguide.python.org/versions/) do python
   - Atualmente 3.9+
4. O [pipx](https://github.com/pypa/pipx) pode te ajudar bastante nesses momentos de instalações globais
   - Que vamos instalar juntos

---

# O ambiente de desenvolvimento

5. O [Poetry](https://python-poetry.org/) (2+) para:
   - Gerenciar os pacotes
   - Instalações de versões do python; e
   - Ambiente virtual
6. [Git](https://git-scm.com/): Para gerenciar versões
7. [Docker](https://www.docker.com/): Para criar um container da nossa aplicação
   - Aula 11 pra frente

> Presentes no [apêndice A](https://fastapidozero.dunossauro.com/4.0/apendices/a_instalacoes/) também :)

---

# Caso seja preciso

Materiais de qualidades e de pessoas incrível que fazem materiais abertos como eu:

1. [Curso de git do teomewhy](https://www.youtube.com/playlist?list=PLvlkVRRKOYFQ3cfYPjLeQ0KvrQ8bG5H11)
2. [Curso de Docker da LinuxTips](https://www.youtube.com/playlist?list=PLf-O3X2-mxDn1VpyU2q3fuI6YYeIWp5rR)
3. [Ajuda para configurar o ambiente - Apêndice A](https://fastapidozero.dunossauro.com/4.0/apendices/a_instalacoes/)

---

# Configuração do ambiente (pipx)

Como nem todo mundo conhece as ferramentas, vamos iniciar com a instalação do pipx. `pipx` é um instalador de pacotes globais do python, geralmente usado para bibliotecas de terminal, que são e`X`ecutáveis.

```
pip install --user pipx    # windows
python -m pipx ensurepath  # windows

sudo apt/dnf install pipx  # linux
pipx ensurepath            # linux
```

> PS: Vamos fazer juntos

---

# Configuração do ambiente (poetry)

Para instalar o poetry você pode fazer a instalação recomendada pelo site ou de forma mais simplificada via pipx

```bash
pipx install poetry
pipx inject poetry poetry-plugin-shell
```

---

# Instalação das ferramentas externas

Isso pode te ajudar a ter menos dificuldade, caso trave em algum lugar

> https://fastapidozero.dunossauro.com/4.0/apendices/a_instalacoes/

---

## Estrutura base do projeto

Vamos criar nossa estrutura do projeto com base na estrutura que o Poetry cria para nós.

```bash
poetry new --flat fast_zero
cd fast_zero
```

isso vai nos gerar essa estrutura:

```bash
.
├── fast_zero
│  └── __init__.py
├── poetry.lock
├── pyproject.yoml
├── README.md
└── tests
   └── __init__.py
```

---

## A versão do python

Uma boa prática é sempre usar a maior versão **possível** do python no projeto. Nem sempre todas as bibliotecas suportam a versão mais recente, mas no nosso caso, tudo funciona na `3.13`:

```shell
poetry python install 3.13  # Mais atual hoje!
poetry env use 3.13         # Pra usar essa versão no projeto
```

---

## A versão do python

Em conjunto com essa instrução, devemos dizer ao poetry que usaremos essa versão em nosso projeto. Para isso vamos alterar o arquivo de configuração do projeto o `pyproject.toml` na raiz do projeto:

```toml
[project]
#...
requires-python = ">=3.13,<4.0"
```

---

## Criando o ambiente virtual

```bash
poetry install
```

---

## Eu sei, você quer FastAPI, veio por isso

Para instalar o fastapi

```bash
poetry add fastapi[standard]
```

---

## Nosso olá mundo [0]

Um código python simples!

```python
# fastzero/app.py
def read_root():
    return {'message': 'Olá Mundo!'}
```

No terminal:

```shell
python -i fastzero/app.py  # -i python interativo
```

---

## Nosso olá mundo [1]

```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}
```

---

## Executando esse código

---

## Para que a execução ocorra, precisamos de um servidor

Isso inicia o servidor de desenvolvimento do FastAPI:

```bash
fastapi dev fast_zero/app.py
```

---

## O "teste"

Se acessarmos http://localhost:8000 podemos ver nossa aplicação

---

## O swagger

Se acessarmos http://localhost:8000/docs podemos ver os endpoinds da nossa aplicação e testar os requests


## O redoc

Se acessarmos http://localhost:8000/redoc podemos ver os endpoinds e suas respostas de forma mais detalhada.

---

# O ambiente de desenvolvimento

> Boas práticas gerais

---

## Para nosso ambiente vamos usar algumas ferramentas diferentes

Ferramentas de desenvolvimento são bastante pessoais. Selecionei 3 que representam bem o que esperamos de um ambiente de desenvolvimento:

- `Ruff`: Um linter e formatador bem poderoso e rápido
- `Pytest`: Para escrevermos os testes
- `Taskipy`: Para não termos que lembrar todos os comandos da aplicação

---

# Ruff

O Ruff é uma ferramenta moderna em python, compatível com os projetos de análise estática escritos e mantidos originalmente pela comunidade no projeto PYCQA e tem duas funções principais:


1. Analisar o código de forma estática (Linter): Efetuar a verificação se estamos programando de acordo com boas práticas do python.
2. Formatar o código (Formatter): Efetuar a verificação do código para padronizar um estilo de código pré-definido.

Para instalar:

```bash
poetry add --group dev ruff
```

---

# Configurando o ruff

Para configurar o ruff montamos a configuração em 3 tabelas distintas no arquivo `pyproject.toml`. Uma para as configurações globais, uma para o linter e uma para o formatador.

A global:

```toml
[tool.ruff]
line-length = 79
extend-exclude = ['migrations']
```

---

# O linter do ruff

Durante a análise estática do código, queremos buscar por coisas específicas. No Ruff, precisamos dizer exatamente o que ele deve analisar.

- `I` ([Isort](https://pycqa.github.io/isort/)): ordenação de imports em ordem alfabética
- `F` ([Pyflakes](https://github.com/PyCQA/pyflakes)): procura por alguns erros em relação a boas práticas de código
- `E` ([pycodestyle](https://pycodestyle.pycqa.org/en/latest/)): erros de estilo de código
- `W` ([pycodestyle](https://pycodestyle.pycqa.org/en/latest/)): avisos sobre estilo de código
- `PL` ([Pylint](https://pylint.pycqa.org/en/latest/index.html)): "erros" em relação a boas práticas de código
- `PT` ([flake8-pytest](https://pypi.org/project/flake8-pytest-style/)): boas práticas do Pytest

---

# Configuração no pyproject.toml

```toml
[tool.ruff.lint]
preview = true
select = ['I', 'F', 'E', 'W', 'PL', 'PT']
```

<style scoped>
blockquote {
	margin-top: 60px;
    font-size: 20px;
}
</style>

> Para mais informações sobre a configuração e sobre os códigos do ruff e dos projetos do PyCQA, você pode checar a [documentação do ruff](https://docs.astral.sh/ruff/rules) ou as documentações originais dos projetos [PyQCA](https://github.com/PyCQA).

---

# Formatador do ruff

A formatação do Ruff praticamente não precisa ser alterada. Pois ele vai seguir as boas práticas e usar a configuração global de `79` caracteres por linha. A única alteração que farei é o uso de aspas simples `'` no lugar de aspas duplas `"`:

```toml
[tool.ruff.format]
preview = true
quote-style = 'single'
```

<style scoped>
blockquote {
	margin-top: 60px;
    font-size: 20px;
}
</style>

> Novamente uma escolha bastante opnionada :)

---

# Usando o ruff

O ruff é feito para ser usado no terminal, alguns comandos são bem interessantes. Como:

- `ruff check .`: Faz a checagem dos termos que definimos antes
- `ruff format .`: Faz a formatação do nosso código sendo as boas práticas

---
# Pytest

O [Pytest](https://docs.pytest.org/) é uma framework de testes, que usaremos para escrever e executar nossos testes. O configuraremos para reconhecer o caminho base para execução dos testes na raiz do projeto `.`:

```bash
poetry add --group dev pytest pytest-cov
```

Também vamos usar o `pytest-cov` para ver o que está ou não coberto pelos testes.

---

# Configuração do pytest

O configuraremos para reconhecer o caminho base para execução dos testes na raiz do projeto `.`:

```toml
[tool.pytest.ini_options]
pythonpath = "."
addopts = '-p no:warnings'
```

Na segunda linha dizemos para o pytest adicionar a opção `no:warnings`. Para ter uma visualização mais limpa dos testes, caso alguma biblioteca exiba uma mensagem de warning, isso será suprimido pelo pytest.

---

## Com isso podemos ver o que está ou não testado

```bash
pytest --cov=fast_zero -vv
coverage html
```

Queremos ver a cobertura do código e os erros de forma verbosa

---

<style scoped>
blockquote {
    font-size: 20px;
}
</style>

# Taskipy

Bom, esses comandos são bem difíceis de lembrar e mais chatos ainda de digitar.


```bash
ruff check .                        # para checar
ruff format .                       # para formatar
fastapi dev fast_zero/app.py        # para rodar a aplicação
pytest --cov=fast_zero -vv          # teste
coverage html                       # cobertura
```
> Por esse motivo você não gosta de usar o shell, eu sei...

Com taskipy podemos fazer esses comando serem uma única palavra

```
task run   # para rodar o servidor
task test  # para executar os testes
```
---

## Instalação e Configuração do taskpy

Instalação:
```bash
poetry add --group dev taskipy
```

Configuração:
```toml
[tool.taskipy.tasks]
lint = 'ruff check'
format = 'ruff format'
run = 'fastapi dev fast_zero/app.py'
test = 'pytest -s -x --cov=fast_zero -vv'
```

---

<style scoped>
blockquote {
	margin-top: 30px;
    font-size: 20px;
}
</style>

## Juntando comandos com taskipy

Alguns comandos fazem mais sentido quando compostos. Queremos fazer mais, com menos comandos:

```toml
[tool.taskipy.tasks]
pre_format = 'ruff check --fix'
pre_test = 'task lint'
post_test = 'coverage html'
```

---

## Cadeia de comandos com taskipy

Em outros momentos, queremos fazer uma coisa, só se a primeira der certo, para isso podemos fazer:

```toml
pre_test = 'task lint'
test = 'pytest -s -x --cov=fast_zero -vv'
post_test = 'coverage html'
```

<div class="mermaid">
graph LR
    pre_task --> task
	task --> post_task
</div>

primeiro a task de lint, se der certo, test, se der certo, coverage :)

---

## Ao final, deve ficar parecido com isso

```toml
[tool.taskipy.tasks]
lint = 'ruff check'
pre_format = 'ruff check --fix'
format = 'ruff format'
run = 'fastapi dev fast_zero/app.py'
pre_test = 'task lint'
test = 'pytest -s -x --cov=fast_zero -vv'
post_test = 'coverage html'
```

---

# Voltando ao código

> Aos testes, na verdade!

---

## Testando o nosso hello world

Dentro da pasta `test` vamos criar um arquivo chamado `test_app.py`

```python
from fastapi.testclient import TestClient
from fast_zero.app import app

client = TestClient(app)
```

---

## Testando de fato

```python
from http import HTTPStatus
from fastapi.testclient import TestClient
from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert 
    assert response.json() == {'message': 'Olá Mundo!'}  # Asset
```

---

# A estrutura de um teste

A estrutura de um teste, costuma contar com 3 ou 4 fases importantes.

- Organizar (Arrange)
- Agir (Act)
- *Afirmar* (Assert)
- *teardown*

---

# Commit

```
pipx run ignr -p python > .gitignore
git init .
gh repo create
```

---

# Exercício

Crie um repositório para acompanhar o curso e suba em alguma plataforma, como [Github](https://github.com/), [gitlab](https://gitlab.com/), [codeberg](https://codeberg.org/), etc. E compartilhe o link na [issue #91 do repositório do curso](https://github.com/dunossauro/fastapi-do-zero/issues/91) para podermos aprender juntos.

> Não se esqueça de responder o [quiz](https://fastapidozero.dunossauro.com/4.0/quizes/aula_01/) dessa aula

---

## Suplementar / Para próxima aula

Caso o mundo dos testes ainda seja um pouco nebuloso para você, recomendo que antes de partir para a próxima aula, você dê uma assistida em algumas lives de python de fora desse curso:

- [Uma introdução aos testes: Como fazer? | Live de Python #232](https://youtu.be/-8H2Pyxnoek)
- [Pytest: Uma introdução - Live de Python #167](https://youtu.be/MjQCvJmc31A)
- [Pytest Fixtures - Live de Python #168](https://youtu.be/sidi9Z_IkLU)


<!-- mermaid.js -->
<script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"></script>
<script>mermaid.initialize({startOnLoad:true,theme:'dark'});</script>
