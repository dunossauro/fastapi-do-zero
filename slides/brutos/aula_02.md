---
marp: true
theme: rose-pine
---

# Introdução ao desenvolvimento WEB
> https://fastapidozero.dunossauro.com/02/

---

# Objetivos dessa aula

- Criar uma base teórica sobre desenvolvimento web
- Apresentar o protocolo HTTP
- Introduzir os conceitos de APIs JSON
- Apresentar o OpenAPI
- Introduzir os schemas usando Pydantic

---

# A WEB

Sempre que nos referimos a aplicações web, estamos falando de aplicações que funcionam em rede.

- Dois ou mais dispositivos interconectados
- Local (**LAN**): como em sua casa ou em uma empresa
- Longa distância (**WAN**): Como diversos roteadores interconectados
- Mundial: como a própria internet

A ideia é a comunicação entre esses dispositivos.

---

# Cliente-Servidor

Quando falamos em comunicação, existem diversos formatos. O mais importante pra nós é o cliente-servidor.

<div class="mermaid">
sequenceDiagram
    participant Cliente
    participant Servidor
    Note left of Cliente: Fazendo a requisição
    Cliente->>Servidor: Crie um usuário
	activate Servidor
    Note right of Servidor: Processa a requisição
    Servidor-->>Cliente: Sucesso na requisição: Usuário criado com sucesso
	deactivate Servidor
    Note left of Cliente: Obtivemos a resposta desejada
</div>

---

# Cliente-servidor

Quando executamos o `fastapi` pelo comando:

```bash
fastapi dev fast_zero/app.py
```

Estamos iniciando um servidor web de desenvolvimento. Por isso a flag `dev`.

<div class="mermaid">
graph LR
    Cliente <--> Servidor
	Servidor <--> A[Aplicação Python]
</div>

---

# O Uvicorn

Ao executar o comando `fastapi dev`, ao fim da mensagem no terminal, vemos:

```bash
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [893203] using WatchFiles
INFO:     Started server process [893207]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Embora o FastAPI seja um ótimo framework web, ele não é um "servidor de aplicação". Por baixo dos panos, ele chama o `Uvicorn`.

---

# Uvicorn

O uvicorn é um servidor de **aplicação**. Um servidor **ASGI**.

A responsabilidade dele é fazer a "cola" entre as chamadas de rede e repassar isso para o "código puro". Uma estrutura de alta performance para trabalhar com chamadas de rede.

<div class="mermaid">
graph LR
    Cliente <--requisita--> Uvicorn
	Uvicorn <--repassa--> A[Aplicação Python]
</div>

Você também poderia usar diretamente o uvicorn:

```bash
uvicorn fast_zero.app:app
```

---

# A rede local

Até esse momento, estamos usando ainda o "loopback", o nosso pc é o cliente e o servidor ao mesmo tempo. O que não é muito prático ainda, pois queremos fazer uma aplicação para diversos clientes.

<div class="mermaid">
graph LR
    ClienteA <--> Uvicorn
    ClienteB <--> Uvicorn
    ClienteC <--> Uvicorn
	Uvicorn <--> A[Aplicação Python]
</div>

---

# Servindo na rede local (LAN)

Saindo do loopback, podemos abrir o servidor do `uvicorn` para rede local:

```bash
fastapi dev fast_zero/app.py --host 0.0.0.0
```

Assim, toda a sua rede domestica (ou empresarial) já podem acessar sua aplicação se souberem o ip.

> Pode chamar alguém de casa, ou acessar por outro dispositivo `http://seu_ip:8000`

---

# Seu IP local com python

```python
>>> import socket
>>> s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
>>> s.connect(("8.8.8.8", 80))
>>> s.getsockname()[0]
'192.168.0.100'
```

> Você também pode usar comandos como `ipconfig`, `ip addr`, ...

---

# O modelo padrão da web

<div class="mermaid">
graph
    A[Web] --> B[URL]
    A --> C[HTTP]
    A --> D[HTML]
</div>

- [URL](https://pt.wikipedia.org/wiki/URL): *Localizador Uniforme de Recursos*. Um endereço de rede pelo qual podemos nos comunicar com um computador na rede.
- [HTTP](https://pt.wikipedia.org/wiki/Hypertext_Transfer_Protocol): um protocolo que especifica como deve ocorrer a comunicação entre dispositivos.
- [HTML](https://pt.wikipedia.org/wiki/HTML): a linguagem usada para criar e estruturar páginas na web.

---

# URL

![center](https://raw.githubusercontent.com/dunossauro/fastapi-do-zero/main/aulas/assets/01/endereco_http_white.png)

---

# URL

![center](https://raw.githubusercontent.com/dunossauro/fastapi-do-zero/main/aulas/assets/02/url_white.png)

---

# HTTP

> TODO


---

# HTML

> TODO

---

# APIs

> TODO

---

# JSON

> TODO

---

# Commit, exercicio e quiz

> TODO


<!-- mermaid.js -->
<script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"></script>
<script>mermaid.initialize({startOnLoad:true,theme:'dark'});</script>
