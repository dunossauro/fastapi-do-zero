---
marp: true
theme: rose-pine
---

# Automatizando os testes com Integração Contínua (CI)

> https://fastapidozero.dunossauro.com/11/

---

### Objetivos da aula

- Compreender a prática de Integração Contínua (CI)
- Aprender a usar o GitHub Actions para criar workflows
- Configurar um pipeline de CI para nossa aplicação que execute testes

---

## Integração contínua (CI)

> TODO: Um blah sobre CI

---

## Fluxo de integração contínua

> TODO: Montar o fluxo

---

## Github Actions

> TODO: Um blah sobre actions

---

## Nosso workflow

<div class="mermaid">
flowchart LR
    Push -- Inicia --> Ubuntu
    Ubuntu -- Execute os --> Passos
	Ubuntu --> Z[Configure as variáveis de ambiente]
	subgraph Passos
      A[Instale a versão 3.11 do Python] --> B[Copie os arquivos do repositório para o ambiente]
	  B --> C[Instale o Poetry]
	  C --> D[Instale as dependência do projeto com Poetry]
	  D --> E[Poetry execute os testes do projeto]
	end
</div>

---

### Iniciando nosso flow

```yaml
name: Pipeline
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Instalar o python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
```

---

### Executando o CI

Pra ver o CI rodando, precisamos fazer commit no repositório:

```bash
git add .
git commit -m "Instalação do Python no CI"
git push
```

> Vamos ver o que acontece [repositório](https://github.com/dunossauro/fast_zero_sync)

---

### Passos do CI

Para executar nossos testes no workflow, precisamos seguir alguns passos essenciais:

1. Instalar o Python
2. Instalar o Poetry
3. Instalar as dependências do projeto
4. Executar os testes

> TODO: diagraminha

---

### Codando esse fluxo

```yaml
    steps:
      - name: Instalar o python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Instalar o poetry
        run: pipx install poetry

      - name: Instalar dependências
        run: poetry install

      - name: Executar testes
        run: poetry run task test
```

---

## Vamos ver o que deu

```bash
git add .
git commit -m "Adicionando passos para executar os testes no CI"
git push
```

> [Repositório](https://github.com/dunossauro/fast_zero_sync)

---

### ERRO!

```shell
Poetry could not find a pyproject.toml file in <path> or its parents
```

---

## Precisamos copiar os arquivos para o CI


```yaml
jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Copia os arquivos do repositório
        uses: actions/checkout@v3

      - name: Instalar o python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      # continua com os passos anteriormente definidos
```

---

### Vamos pra mais um erro!

```bash
git add .
git commit -m "Adicionando o checkout ao pipeline"
git push
```

> [Repositório](https://github.com/dunossauro/fast_zero_sync)

---

## Variáveis de ambiente no CI

**USEM O GH**, dito isso...

```shell
gh secret set -f .env
```

> [Caso contrário](http://localhost:8080/11/#definindo-secrets-no-repositorio)

---

## Dando acesso o CI

```yaml
jobs:
  test:
    runs-on: ubuntu-latest

    env:
      DATABASE_URL: ${{ secrets.DATABASE_URL }}
      SECRET_KEY: ${{ secrets.SECRET_KEY }}
      ALGORITHM: ${{ secrets.ALGORITHM }}
      ACCESS_TOKEN_EXPIRE_MINUTES: ${{ secrets.ACCESS_TOKEN_EXPIRE_MINUTES }}
```

---

### Outro commit ...

```bash
git add .
git commit -m "Adicionando as variáveis de ambiente para o CI"
git push
```

---

## Quiz

Não esqueça de responder o [quiz](http://localhost:8080/quizes/aula_11/)!


<!-- mermaid.js -->
<script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"></script>
<script>mermaid.initialize({startOnLoad:true,theme:'dark'});</script>
