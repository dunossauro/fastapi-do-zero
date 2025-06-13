---
marp: true
theme: rose-pine
---

# Automatizando os testes com Integração Contínua (CI)

> https://fastapidozero.dunossauro.com/estavel/12/

---

### Objetivos da aula

- Compreender a prática de Integração Contínua (CI)
- Aprender a usar o GitHub Actions para criar workflows
- Configurar um pipeline de CI para nossa aplicação que execute testes

---

## Integração contínua (CI)

Integração Contínua (CI) é uma prática de desenvolvimento que envolve a integração regular do código-fonte ao repositório principal, acompanhada de testes automatizados para garantir a qualidade.

<div class="mermaid">
flowchart LR
  pull_request --> id0["Cria um ambiente"]
  push --> id0
  id0 --> Testes
  Testes --> passa{passa?}
  passa --> sim
  sim --> id2["Integra normalmente"]
  passa --> não
  não --> id1["Envia uma notificação"]
</div>

---

## Github Actions

Entre as ferramentas disponíveis para CI, o [GitHub Actions](https://github.com/features/actions) é um serviço do GitHub que automatiza workflows dentro do seu repositório. Você pode configurar o GitHub Actions para executar ações específicas — como testes automatizados — cada vez que um novo código é commitado no repositório.

---

### Nosso workflow

<div class="mermaid">
flowchart RL
    Push -- Inicia --> Ubuntu
    Ubuntu -- Execute os --> Passos
	Ubuntu --> Z[Configure as variáveis de ambiente]
	subgraph Passos
      A[Instale a versão 3.13 do Python] --> B[Copie os arquivos do repositório para o ambiente]
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
          python-version: '3.13'
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

<div class="mermaid">
flowchart LR
   Python["1: Python instalado"] --> Poetry["2: Poetry instalado"]
   Poetry --> Deps["3: Instalar as dependências via Poetry"]
   Deps --> Testes["4: Executar os testes via Poetry"]
</div>

---

### Codando esse fluxo

```yaml
    steps:
      - name: Instalar o python
        uses: actions/setup-python@v5
        with:
          python-version: '3.13'

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
        uses: actions/checkout@v4

      - name: Instalar o python
        uses: actions/setup-python@v5
        with:
          python-version: '3.13'

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

> [Caso contrário](https://fastapidozero.dunossauro.com/11/#definindo-secrets-no-repositorio)

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

Não esqueça de responder o [quiz](https://fastapidozero.dunossauro.com/estavel/quizes/aula_12/)!


<!-- mermaid.js -->
<script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"></script>
<script>mermaid.initialize({startOnLoad:true,theme:'dark'});</script>
