---
marp: true
theme: rose-pine
---

# Fazendo deploy no Fly.io

> https://fastapidozero.dunossauro.com/12/

---

## Objetivos dessa aula

- Entender o que é o Fly.io e como usar sua CLI
- Aprender a fazer o deploy de uma aplicação Docker no Fly.io
- Configurar uma instância do PostgreSQL no Fly.io
- Configurar as variáveis de ambiente
- Rodar as migrações em produção

---

## Fly.io

> Um blah sobre o fly

---

## PaaS

> Um blah sobre o PaaS

---

## Uma notícia incrível <3

Temos um cumpom de crédito para usar o fly:
https://fly.io/fastapi-do-zero-2024


Obrigado de mais Kátia Nakamura <3 <3 <3

---

## Deploy

> Um blah sobre o Deploy

---

## Flyctl

> Um blah sobre o flyctl


```bash
flyctl version
```

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

Não esqueça de responder ao [quiz](https://fastapidozero.dunossauro.com/quizes/aula_12/) dessa aula!

---
## Commit

```bash
git add .
git commit -m "Adicionando arquivos gerados pelo Fly"
git push
```

<script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"></script>
<script>mermaid.initialize({startOnLoad:true,theme:'dark'});</script>
 
