# Uma introdução a testes de carga com Locust

<quiz>
Qual é o principal objetivo de um teste de carga em uma aplicação?
- [x] Medir quantos usuários simultâneos a aplicação suporta
- [ ] Testar se a aplicação funciona corretamente
- [ ] Verificar a cobertura de testes unitários
- [ ] Garantir que o código está bem documentado
</quiz>

---

<quiz>
O que o Locust utiliza para representar um usuário da aplicação?
- [x] HttpUser
- [ ] FastAPIUser
- [ ] TestClient
- [ ] Worker
</quiz>

---

<quiz>
No Locust, o que representa a anotação `@task` dentro de uma classe `HttpUser`?
- [ ] Um teste unitário
- [x] Uma ação ou endpoint que o usuário irá acessar
- [ ] Um comando para iniciar o servidor
- [ ] Um tipo de requisição GET
</quiz>

---

<quiz>
Qual das métricas abaixo indica o número de requisições processadas por segundo em tempo real?
- [ ] Median (ms)
- [ ] Average (ms)
- [x] Current RPS
- [ ] Requests
</quiz>

---

<quiz>
Se o `Current Failures/s` começa a subir, o que isso geralmente indica?
- [ ] A aplicação está estável
- [x] Que o sistema está atingindo algum limite ou gargalo
- [ ] Que os testes unitários falharam
- [ ] Que o banco de dados não está configurado
</quiz>

---

<quiz>
Qual métrica é mais útil para entender o comportamento típico da aplicação, ignorando picos extremos?
- [ ] Average (ms)
- [ ] Max (ms)
- [x] Median (ms)
- [ ] Min (ms)
</quiz>

---

<quiz>
O que o percentil 95 (p95) indica em um teste de carga?
- [ ] O tempo médio de todas as requisições
- [ ] O tempo mínimo de resposta
- [x] Que 95% das requisições responderam em até aquele tempo
- [ ] Que 5% das requisições falharam
</quiz>

---

<quiz>
Durante um teste de carga, se a média (`Average`) está muito maior que a mediana (`Median`) e o p99 dispara, isso indica:
- [ ] Sistema rápido e estável
- [x] Degradação na aplicação, geralmente nos casos extremos
- [ ] Que o teste falhou
- [ ] Que mais usuários precisam ser adicionados
</quiz>

---

<quiz>
Qual a principal diferença entre testes funcionais (pytest) e testes de carga (Locust)?
- [x] Testes funcionais verificam se a aplicação funciona; testes de carga verificam a performance sob múltiplos usuários
- [ ] Testes funcionais usam Docker; testes de carga não
- [ ] Testes de carga são feitos apenas em produção
- [ ] Testes funcionais medem RPS e latência
</quiz>

---

<quiz>
Por que é importante analisar os percentis (p95, p99) ao invés de apenas a média em um teste de carga?
- [ ] Percentis indicam erros de código
- [x] Porque eles mostram os extremos e a experiência de usuários afetados por picos de latência
- [ ] Percentis substituem a necessidade de olhar para o RPS
- [ ] Porque a mediana ignora totalmente a performance
</quiz>
