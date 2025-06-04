---
marp: true
theme: rose-pine
---

# Fazendo deploy no Fly.io

> https://fastapidozero.dunossauro.com/estavel/13/

---

## Objetivos dessa aula

- Entender o que é o Fly.io e como usar sua CLI
- Aprender a fazer o deploy de uma aplicação Docker no Fly.io
- Configurar uma instância do PostgreSQL no Fly.io
- Configurar as variáveis de ambiente
- Rodar as migrações em produção

---

## Deploy

A ultima parte do processo do código, **colocar em produção**.

No caso da nossa API, é "soltar ela no mundo" para que as outras pessoas usar. Liberar na internet.

---

## Fly.io

O Fly.io é uma plataforma de deploy que nos permite fazer o lançamento nossas aplicações na nuvem e que oferece serviços para diversas linguagens de programação e frameworks como Python e Django, PHP e Laravel, Ruby e Rails, Elixir e Phoenix, etc.

Ao mesmo tempo, em que permite que o deploy de aplicações em containers docker também possam ser utilizadas, como é o nosso caso. Além disso, o Fly disponibiliza bancos de dados para serem usados em nossas aplicações, como PostgreSQL e Redis.

---

## Mas, Fly.io?

A ideia de usar o fly.io é que ele oferece uma plataforma simplificada para deploy. Sendo necessário nos preocuparmos somente o container Docker da nossa aplicação.

O restante das configurações fica a encargo deles.

---

## PaaS - Platform as a service

Uma plataforma como serviço significa que contratamos um serviço de plataforma.

Por plataforma entenda que o serviço contratado vai cuidar de:

- Segurança
- Rede
- Disponibilidade
- Atualizações / Manutenção
- ...

Entregamos container ao serviço e damos "play"

---

## Uma notícia incrível <3

Temos um cumpom de crédito para usar o fly:
https://fly.io/fastapi-do-zero-2024


Obrigado de mais Kátia Nakamura <3 <3 <3

---

## Flyctl

O flyctl é um CLI do fly que podemos usar para fazer as funções administrativas da aplicação pelo terminal:

```bash
flyctl version
```

> Caso precise instalar o [flyctl](https://fly.io/docs/flyctl/)

---

## Autenticação via CLI

```bash
flyctl auth login
```

---

## Configuração para o deploy

```bash
flyctl launch --no-deploy
```

Responda um absoluto Y aqui:
```bash
# ...
? Do you want to tweak these settings before proceeding? (y/N) 
```

---

## Manuzeando nossa variáveis de ambiente

```bash
flyctl secrets list
flyctl secrets set DATABASE_URL=???
flyctl secrets set ALGORITHM="HS256"
flyctl secrets set SECRET_KEY="your-secret-key"
flyctl secrets set ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Fazendo o deploy

```bash
fly deploy --local-only --ha=false

# ...

Visit your newly deployed app at https://fastzeroapp.fly.dev/
```

---

## Executando as migrações

```bash
flyctl ssh console -a fastzeroapp -C "poetry run alembic upgrade head"
```

---

## Quiz

Não esqueça de responder ao [quiz](https://fastapidozero.dunossauro.com/estavel/quizes/aula_13/) dessa aula!

---
## Commit

```bash
git add .
git commit -m "Adicionando arquivos gerados pelo Fly"
git push
```

<script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"></script>
<script>mermaid.initialize({startOnLoad:true,theme:'dark'});</script>
 
