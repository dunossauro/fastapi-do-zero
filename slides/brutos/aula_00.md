---
marp: true
theme: rose-pine
---

# FastAPI do zero `2025`

> https://fastapidozero.dunossauro.com/

---

# Nosso roteiro de hoje

- Sobre o curso
- Sobre o valor do curso? **é de graça MESMO?**
- Como será disponibilizado?
- Pré-requisitos
- Programação
- O projeto final

---

# Sobre o curso

> https://fastapidozero.dunossauro.com/#sobre-o-curso

---

# É mesmo um curso sobre FastAPI?

A ideia por trás desse material não é só o FastAPI, mas sobre as tecnologias python que criam um ecossistema para desenvolvimento web.

- Fundamentos de desenvolvimento web
- FastAPI
- Pydantic
- Uvicorn
- SQLAlchemy
- JWT
- asyncIO

---

# É também sobre algumas práticas comuns

- Ambiente e ferramentas de desenvolvimento
  - poetry, taskipy, ruff, ...
- Testes
  - pytest, fixtures, coverage, factory-boy, freezegun, testcontainers, ...
- Operações
  - containers, integração contínua, deploy, ...

---

# O que vamos construir?

Vocês sabem que eu sou o "pai da teoria". Então, decidir fazer uma coisa um pouco diferente.

- Um projeto prático
- Do zero
- Com testes
- Até o deploy

---

# Como será o projeto?

Vamos construir um "todo list", uma ferramenta para gerenciar tarefas "a fazer".

- Eu sei, isso é bastante clichê
- Mas, vamos fazer isso com estilo
- O mais próximo de um projeto entregável
- """focado em práticas do mercado"""

---

# Acessar alguns links aqui :)

- O projeto final, deve se parecer com isso: [fast_zero](https://github.com/dunossauro/fastapi-do-zero/tree/v4.0/codigo_das_aulas/13)
- Em produção: [no deploy](https://fastzeroapp.fly.dev/)
- Ambiente de CI: [Github Actions](https://github.com/dunossauro/fast_zero/actions)

---

<style scoped>
blockquote {
	margin-top: 60px;
    font-size: 20px;
}
</style>

# Como está estruturado?

O curso ao todo tem 14 aulas. Todas elas têm:

- Uma aula em texto: [exemplo](https://fastapidozero.dunossauro.com/01/)
- Exercícios para fixação prática: [exemplo](https://fastapidozero.dunossauro.com/04/#exercicios)
- Quizes para fixação teórica: [exemplo](https://fastapidozero.dunossauro.com/quizes/aula_01/)

> Recomendo que você tire um tempo na semana para responder aos quizes e a feitura dos exercícios

---

# Sobre o que não vamos falar?

### O curso é totalmente focado em backend e APIs JSON

- Não construiremos um cliente (html, gui, mobile, ...)
- Não entraremos no contexto de CD (Continuous Deploy)
- Não faremos deploy de modelos (IA)
- Não falaremos de integrações (serviços além do banco de dados)
- Nem mesmo sobre bots

> Embora, com a base construída aqui, você deve ser capaz de seguir esses caminhos após o curso

---

# O curso é mesmo de **graça**?

> https://fastapidozero.dunossauro.com/#esse-curso-e-gratuito

---

<style scoped>
h1 {
  font-size: 510px;
  text-align: center;
}
</style>

# SIM!

---

<style scoped>
h1 {
  font-size: 300px;
  text-align: center;
}
</style>

# SIM!

> Porém...

---

# Você pode contribuir financeiramente com ele

De diversas formas:

- Pela campanha de financiamento da Live de Python no apoia.se
- Pelo clube de membros do youtube
- Pelo pix (pix.dunossauro@gmail.com)

> Isso me ajuda a pagar as contas e me manter durantes esse curso. Considera apoiar :)

---

# Como o curso será disponibilizado?
> https://fastapidozero.dunossauro.com/#onde-o-curso-sera-disponibilizado


---

<style scoped>
ul {
  font-size: 28px;
}
</style>


# Como o curso será disponibilizado?

1. Em texto, para quem prefere ler
    - https://fastapidozero.dunossauro.com/
2. Em aulas síncronas: Para quem precisa do compromisso de estar junto
    - Datas dos encontros: https://fastapidozero.dunossauro.com/4.0/aulas/2025/
	- **Estamos aqui!**
	- A lives ficarão salvas para ver depois :)
3. A edição de 2024 está completamente disponível, se estiver com pressa
   - [playlist](https://www.youtube.com/playlist?list=PLOQgLBuj2-3IuFbt-wJw2p2NiV9WTRzIP)

---

# Pré-requisitos para acompanhar
> https://fastapidozero.dunossauro.com/#pre-requisitos

---

## Algumas coisas importantes

Como o objetivo desse curso é conversar sobre um framework web feito em python. É importante, para acompanhar, que você tenha noções sobre:

- O funcionamento de funções: como criar e usar: [uma referência](https://youtu.be/0yXPQZvlgrk)
- O funcionamento das estruturas de dados: como listas, dicionários e etc;
- Uma pitada sobre objetos: saber o que são métodos e atributos [uma referência](https://www.youtube.com/playlist?list=PLOQgLBuj2-3L_L6ahsBVA_SzuGtKre3OK)
- Classes de dados: o funcionamento mínimo sobre dataclasses: [uma referência](https://www.youtube.com/watch?v=NtZY3AmsBSk)

---

# Algumas outras coisas **não essenciais**

Alguns outros tópicos não relativos a Python também serão abordados. Então, é interessante que você tenha algum entendimento básico sobre:

- Desenvolvimento Web e APIs RESTful
- Banco de dados / SQL
- git
- docker

---

# Programação

> https://fastapidozero.dunossauro.com/4.0/aulas/2025/

---

# Nossos encontros síncronos

Nossos encontros acontecerão às **terças e quintas** com duração de **2h**. Entre às **20h e 22h**.

Com chat aberto para tirar dúvidas enquanto a aula acontece.

- [iCal](https://calendar.google.com/calendar/ical/6d04fd6ec76625bcd265875fdc5e4670a001c60f53bc96b596a43394b8c78ca0%40group.calendar.google.com/public/basic.ics)
- [Google Agenda](https://calendar.google.com/calendar/u/0?cid=NmQwNGZkNmVjNzY2MjViY2QyNjU4NzVmZGM1ZTQ2NzBhMDAxYzYwZjUzYmM5NmI1OTZhNDMzOTRiOGM3OGNhMEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t)


---

# Algumas recomendações

Sei que existem estilos diferentes de estudo que funcionam melhor para cada pessoa. Mas acho importante:

- Dar uma lida no material antes, para aproveitar melhor as lives e tirar dúvidas
- Fazer os quizes e os exercícios
- Postar suas dúvidas no nosso grupo do [telegram](https://t.me/fastapicomdunossauro)

---

# O projeto final
> https://fastapidozero.dunossauro.com/4.0/15/

---

# Projeto final

Ao final do curso, temos um material bem descritivo, em um formato de um teste técnico (sim, aqueles que as empresas cobram). Pode ser interessante fazê-lo. Tanto para fixação, quanto para fazer suas próprias escolhas de design e estruturas.

As instruções estão aqui: https://fastapidozero.dunossauro.com/4.0/15/

---

# Considerações **MUITO** importantes

O texto anda em um ritmo bem mais rápido que os vídeos.

Logo, a versão do texto que usaremos agora é a `4.0.*`

Atualmente é a tag 4.0.1, os fixes estão todos na versão 4.0:

https://fastapidozero.dunossauro.com/4.0

---

<style scoped>
h2 {
  font-size: 100px;
  text-align: center;
}
h3 {
  text-align: center;
}
p {
	margin-top: 60px;
    font-size: 20px;
    text-align: center;
}
</style>


# Por hoje é só

## XOXO
### http://dunossauro.com
### https://fastapidozero.dunossauro.com/

Nos vemos na primeira aula!
