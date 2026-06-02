# Exercícios da aula 01

## Exercício 01

Crie um repositório para acompanhar o curso e suba em alguma plataforma, como [Github](https://github.com/), [gitlab](https://gitlab.com/), [codeberg](https://codeberg.org/), etc. E compartilhe o link no [repositório do curso](https://github.com/dunossauro/fastapi-do-zero/issues/91) para podermos aprender juntos.


## Exercício 02

Adicione o `typos` para análisar gramática em inglês para ser executado antes da etapa de `lint` (`pre_lint`) no `pyproject.toml`.

### Solução

O objetivo aqui é automatizar a verificação ortográfica para que ela rode sempre de forma automática antes do `ruff check`. Para fazer isso, vamos usar o sistema de ganchos (hooks) em cadeia do Taskipy.


Abra o seu arquivo `pyproject.toml` e navegue até a tabela `[tool.taskipy.tasks]`.

Basta adicionar a tarefa `pre_lint` apontando para o comando `typos`. O Taskipy vai entender automaticamente que, por causa do prefixo `pre_`, ele deve rodar o typos antes do comando `lint`.

O seu bloco de tarefas deve ficar exatamente assim:

```toml title="pyproject.toml"
[tool.taskipy.tasks]
pre_lint = "typos"               # (1)!
lint = "ruff check"
pre_format = "ruff check --fix"
format = "ruff format"
run = "fastapi dev fast_zero/app.py"
pre_test = "task lint"
test = "pytest -v"
post_test = "coverage html"
```

1. Nova tarefa adicionada. Agora, sempre que você digitar `task lint`, o `typos` será executado primeiro.

Para garantir que está funcionando, execute o linter no seu terminal:

```shell title="$ Execução no terminal!"
task lint
```
