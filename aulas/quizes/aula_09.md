# 09 - Tornando o sistema de autenticação robusto

<quiz>
Sobre o Factory-boy. O que siginifica a classe Meta?

```python hl_lines="4"
class UserFactory(factory.Factory):
    class Meta:
        model = User
```
- [ ] Diz que será usada uma metaclasse
- [x] Explica ao Factory qual objeto ele deve se basear
- [ ] Extente a classe Factory com os parâmetros de Meta
</quiz>

<quiz>
Ainda sobre o Factory-boy. O que siginifica `factory.Sequence`?
- [ ] Criará uma sequência de Metas
- [x] Adicionará +1 em cada objeto criado
- [ ] Monta uma sequência de objetos
- [ ] Cria um novo objeto do factory
</quiz>


<quiz>
Continuando o Factory-boy. O que siginifica `factory.LazyAttribute`?
- [x] Diz que o atributo será criado em tempo de execução
- [x] Diz que o atributo usará outros atributos para ser inicializado
- [x] Usa outros campos para ser composto
- [ ] Cria um atributo independênte
</quiz>

<quiz>
O que faz o gerenciador de contexto `freeze_time`?

```python hl_lines="1"
with freeze_time('2023-07-14 12:00:00'):
    response = client.post(
        '/auth/token',
        data={'username': user.email, 'password': user.clean_password},
    )
```

- [x] Pausa o tempo nas instruções dentro do 'with'
- [ ] Congela o tempo da função toda
- [ ] Muda a hora do computador para a do bloco
</quiz>

<quiz>
O que levanta o erro `ExpiredSignatureError`?
- [ ] Quando deu erro no valor de 'exp'
- [ ] Quando não deu certo avaliar a claim de 'exp'
- [x] Quando a claim de 'exp' tem um tempo expirado
</quiz>
