# Exercícios da aula 01

## Exercício 01

Crie um repositório para acompanhar o curso e suba em alguma plataforma, como [Github](https://github.com/), [gitlab](https://gitlab.com/), [codeberg](https://codeberg.org/), etc. E compartilhe o link no [repositório do curso](https://github.com/dunossauro/fastapi-do-zero/issues/91) para podermos aprender juntos.


## Exercício 02

Adicione o `typos` para analisar gramática em inglês para ser executado antes da etapa de lint, transformando ela em uma sequência que rode o `typos` e o `ruff check` na tabela `[tool.poe.tasks]` do seu arquivo `pyproject.toml`.

### Solução

O objetivo aqui é automatizar a verificação ortográfica para que ela rode sempre de forma automática antes do `ruff check`. Para fazer isso, vamos transformar o nosso comando `lint` em uma sequência no Poe.

Abra o seu arquivo `pyproject.toml` e navegue até a tabela `[tool.poe.tasks]`.

Como o `lint` antes era apenas uma string simples (`lint = { cmd = "ruff check" }`), precisamos alterá-lo para usar a propriedade `.sequence`, passando uma lista com o `typos` primeiro e o `ruff check` logo em seguida.
 
 O seu bloco de tarefas deve ficar exatamente assim:

```toml title="pyproject.toml" hl_lines="2-5"
[tool.poe.tasks]
lint.sequence = [
  "typos", # (1)!
  { cmd = "ruff check" },
]
format.sequence = [
  { cmd = "ruff check --fix" },
  { cmd = "ruff format" },
]
serve = "fastapi dev fast_zero/app.py"
test.sequence = [
  "lint",
  { cmd = "pytest -s -x -vv $POE_EXTRA_ARGS" },
  { cmd = "coverage html --show-contexts" },
]
```

1. O comando `typos` foi adicionado como o primeiro passo da sequência. Agora, sempre que você rodar o lint, ele verificará a ortografia antes de passar para as regras do ruff.

Para garantir que está funcionando, execute o linter no seu terminal:

```shell title="$ Execução no terminal!"
poetry lint
```
