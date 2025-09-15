# B - Próximos passos

Esse apêndice se destina a mostrar alguns exemplos de código da página de despedida/próximos passos. Alguns exemplos simples de como fazer algumas tarefas que não trabalhamos durante o curso.

## Templates

O FastAPI conta com um recurso de carregamento de arquivos estáticos, como CSS e JS. E também permite a renderização de templates com [jinja](https://jinja.palletsprojects.com/en/3.1.x/){:target="_blank"}.

Os templates são formas de passar informações para o HTML diretamente dos endpoints. Mas, comecemos pela estrutura. Criaremos dois diretórios. Um para os templates e um para os arquivos estáticos:

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


Para unir os arquivos estáticos e os templates na aplicação, podemos aplicar o seguinte bloco de código:

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

![](../assets/apendices/ola_mundo_com_templates.png){: .center .shadow }

## Tarefas em segundo plano (Background)

Em algumas aplicações, é preciso realizar tarefas que possam ser feitas sem atrapalhar o funcionamento principal do programa. É útil para enviar e-mails, processar arquivos ou fazer cálculos demorados, mas sem impactar a experiência do usuário, que pode continuar interagindo com a aplicação.

O FastAPI oferece suporte nativo para a execução de tarefas em segundo plano usando o objeto `BackgroundTasks`. Esse objeto permite que você adicione funções que serão executadas após a resposta ser enviada ao cliente. Dessa forma, o cliente não precisa esperar que a tarefa seja concluída para continuar suas interações.

### Exemplo de implementação

No exemplo a seguir, criamos uma tarefa simples que dorme por um tempo especificado e retorna uma resposta indicando que a requisição foi recebida e está sendo processada.

```python title="app.py"
from time import sleep

from fastapi import BackgroundTasks, FastAPI


app = FastAPI()


def tarefa_em_segundo_plano(tempo=0):#(1)!
    sleep(tempo)  # Simula um processo demorado


@app.get('/segundo-plano/{tempo}')
def segundo_plano(tempo: int, task: BackgroundTasks):#(2)!
    task.add_task(tarefa_em_segundo_plano, tempo)#(3)!
    return {'message': 'Sua requisição está sendo processada!'}
```

1. **Função de Tarefa:** A função `tarefa_em_segundo_plano` simula uma tarefa demorada, utilizando a função `sleep` para interromper a execução por um tempo determinado pelo parâmetro `tempo`. Essa função pode ser qualquer função Python que você deseje rodar em segundo plano.
   
2. **Recebendo BackgroundTasks:** O tipo `BackgroundTasks` é injetado automaticamente no endpoint, e ele permite que você adicione tarefas ao loop de eventos do FastAPI. Ao receber esse tipo, o endpoint poderá adicionar tarefas para execução em segundo plano, sem afetar a resposta imediata ao cliente.

3. **Adicionando a tarefa ao background:** A função `.add_task()` do `BackgroundTasks` é usada para adicionar a função `tarefa_em_segundo_plano` ao evento em segundo plano, passando o parâmetro necessário (`tempo`, no caso). Assim, quando o cliente acessar o endpoint, a tarefa será iniciada em segundo plano enquanto a resposta já é enviada para ele.

### Como funciona a execução

Quando um cliente acessa o endpoint `/segundo-plano/{tempo}`, o FastAPI envia imediatamente a resposta `{'message': 'Sua requisição está sendo processada!'}`. A tarefa, que simula um processo demorado, é executada em segundo plano, sem que o cliente tenha que aguardar sua conclusão.

Isso permite que você realize operações demoradas sem prejudicar a experiência do usuário, que pode seguir usando a aplicação enquanto a tarefa está em andamento.

## Eventos de ciclo de vida

Os eventos de ciclo de vida são formas de iniciar ou testar alguma condição antes de a aplicação ser de fato inicializada. Você pode criar validações, como saber se outra aplicação está de pé, configurar coisas antes de a aplicação ser iniciada, como iniciar o banco de dados, etc.

Da mesma forma, alguns casos para antes de a aplicação ser finalizada também podem ser criadas. Como garantir que todas as [tarefas em segundo plano](#tarefas-em-segundo-plano-background) estejam de fato finalizadas antes da aplicação parar de rodar.

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
