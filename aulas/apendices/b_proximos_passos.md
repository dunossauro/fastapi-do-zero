# B - Próximos passos

Esse apêndice se destina a mostrar alguns exemplos de código da página de despedida/próximos passos. Alguns exemplos simples de como fazer algumas tarefas que não dizemos durante o curso.

## Templates

O FastAPI conta com um recurso de carregamento de arquivos estáticos, como css e js. E também permite a renderização de templates com [jinja](https://jinja.palletsprojects.com/en/3.1.x/){:target="_blank"}.

Os templates são formas de passar informações para o html diretamente dos endpoints. Mas, vamos começar pela estrutura. Criaremos dois diretórios. Um para os templates e um para os arquivos estáticos:

```python title="Estrutura dos arquivos"
.
├── app.py
├── static #(1)!
│  └── style.css
└── templates #(2)!
   └── index.html
```

1. Diretório para arquivos estáticos.
2. Diretório para os templates do jinja


Vamos adicionar um arquivo de estilo bastante simples, somente para ver o efeito da configuração:

```css title="static/style.css"
h1 {
    text-align: center;
}
```

E um arquivo html usando a tag dos templates:

```html title="templates/index.html"
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8"/>
    <title>index.html</title>
    <link href="static/style.css" rel="stylesheet"/>
  </head>
  <body>
    <h1>Olá {{ nome }}</h1> <!-- (1)! -->
  </body>
</html>
```
{% raw %}
1. Nomes dentro de `{{ }}` são variáveis que serão preenchidas pelo contexto

Todas as variáveis incluídas em `{{ variável }}` são passadas pelo endpoint no momento de retornar o template jinja. Com isso, podemos incluir valores da aplicação no HTML.
{% endraw %}


Para unir os arquivos estáticos e os templates na aplicação podemos aplicar o seguinte bloco de código:

```python title="app.py"
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Diretório contendo arquivos estáticos
app.mount('/static', StaticFiles(directory='static'), name='static')#(1)!

# Diretório contendo os templates Jinja
templates = Jinja2Templates(directory='templates')#(2)!


@app.get('/{nome}', response_class=HTMLResponse)
def home(request: Request, nome: str):#(3)!
    return templates.TemplateResponse(#(4)!
        request=request, name='index.html', context={'nome': nome}
    )
```

1. O método `.mount` cria um endpoint `/static` para retornar os arquivos no diretório `static`.
2. `Jinja2Templates` mapeia um diretório em nossa aplicação onde armazenamos templates jinja para serem lidos pela aplicação.
3. O objeto `Request` do FastAPI é o objeto que representa corpo da requisição e seu escopo.
4. O método `TemplateResponse` se encarrega de dizer qual o nome (`name`) do template que será renderizado no html e `context` é um dicionário que passa as variáveis do endpoint para o arquivo html.

---

Para que os templates sejam renderizados pelo FastAPI precisamos instalar o jinja:

```shell title="$ Execução no terminal!"
poetry add jinja2
```

E executar nosso projeto com:

```shell title="$ Execução no terminal!"
task run
```

Desta forma, ao acessar o endpoint pela API, temos a junção de templates e estáticos acontecendo:

![](/assets/apendices/ola_mundo_com_templates.png){: .center .shadow }


## Asyncio

O FastAPI tem suporte nativo para programação assíncrona. A única coisa que precisa ser feita para isso, a nível do framework (não incluindo as dependências) é adicionar a palavra reservada `#!python async` no início dos endpoints. 

Da seguinte forma:

```python title="app.py"
from asyncio import sleep

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def home():#(1)!
    await sleep(1)#(2)!
    return {'message': 'Olá mundo!'}
```
1. Criação de uma função assíncrona
2. Contexto de escalonamento usando `await`

O escalonamento do loop durante as chamadas nos endpoints pode ser feito por meio da palavra reservada `#!python await`.

---

Para que os testes sejam executados de forma assíncrona, precisamos instalar uma extensão do pytest:

```shell title="$ Execução no terminal!"
poetry add pytest-asyncio
```

Dessa forma podemos executar funções de teste que também são assíncronas usando um marcador do pytest:
```python title="test_app.py"
from fastapi.testclient import TestClient

from app import app

import pytest


@pytest.mark.asyncio #(1)!
async def test_async():
    client = TestClient(app)
    response = client.get('/')

    assert response.json() == {'message': 'Olá mundo!'}
```

1. Marcador para executar a função de teste dentro de um loop de eventos


## Tarefas em segundo plano (Background)

Tarefas em segundo plano...

```python title="app.py"
from time import sleep

from fastapi import BackgroundTasks, FastAPI


app = FastAPI()


def tarefa_em_segundo_plano(tempo=0):#(1)!
    sleep(tempo)


@app.get('/segundo-plano/{tempo}')
def segundo_plano(tempo: int, task: BackgroundTasks):#(2)!
    task.add_task(tarefa_em_segundo_plano, tempo)#(3)!
    return {'message': 'Sua requisição está sendo processada!'}
```

1. Uma função qualquer em python que será executada a qualquer momento
2. O tipo `BackgroundTasks` deve ser passado ao endpoint para que ele tenha a possibilidade de adicionar uma tarefa ao loop de eventos
3. O método `.add_task` adiciona a tarefa (função) ao loop de eventos.

## Eventos de ciclo de vida

Os eventos de ciclo de vida são formas de iniciar ou testar alguma condição antes da aplicação ser de fato inicializada. Você pode criar validações, como saber se outra aplicação está de pé. Configurar coisas antes da aplicação ser iniciada, como iniciar o banco de dados, etc...

Da mesma forma alguns casos para antes da aplicação ser finalizada também podem ser criadas. Como garantir que todas as [tarefas em segundo plano](#tarefas-em-segundo-plano-background) estejam de fato finalizadas antes da aplicação parar de rodar.

```python title="app.py"
from logging import getLogger
from time import sleep

from fastapi import FastAPI


logger = getLogger('uvicorn')

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info('Iniciando a aplicação')#(1)!
    yield  # Executa a aplicação
    logger.info('Finalizando a aplicação')#(2)!


app = FastAPI(lifespan=lifespan)#(3)!
```

1. Log que será emitido antes da aplicação ser iniciada
2. Log que será emitido antes da aplicação ser finalizada
3. O parâmetro `lifespan` recebe uma função assíncrona com `yield` para uma condição de parada. Assim como uma fixture do pytest.

Podemos observar que os logs foram adicionados ao uvicorn antes e depois da execução da aplicação:

```shell title="$ Execução no terminal!" hl_lines="4 11"
uvicorn app:app
INFO:     Started server process [254037]
INFO:     Waiting for application startup.
INFO:     Iniciando a aplicação
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
# Apertando Ctrl + C
^C
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Finalizando a aplicação
INFO:     Application shutdown complete.
INFO:     Finished server process [254037]
```
