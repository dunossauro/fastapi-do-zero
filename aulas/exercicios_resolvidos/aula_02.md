# Exercícios da aula 02

## Exercício 01

Crie um endpoint que retorne "olá mundo" usando HTML e escreva seu teste.

> Dica: para capturar a resposta do HTML do cliente de testes, você pode usar `#!python response.text`


### Solução

Para criação do endpoint retornando HTML devemos alterar a classe de resposta padrão do FastAPI para `HTMLResponse`:

```python title="Implementação do endpoint"
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/', response_class=HTMLResponse)
def read_root():
    return """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""
```

O teste que faz a validação do valor retornado pelo endpoint não precisa ser muito robusto. A ideia principal do exercício é somente validar se estamos retornando o "Olá Mundo" em formato de HTML:

```python title="Implementação do teste"
from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ola_mundo_em_html():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo </h1>' in response.text
```

O `response.text` é um método do cliente de testes do FastAPI que converte os bytes de resposta em string.
