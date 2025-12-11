# 08 - Tornando o projeto assíncrono

<quiz>
Escalonamento no asyncio é a capacidade do código de:
- [ ] Executar tarefas simultaneamente
- [ ] Alternar entre a execução de funções
- [ ] Fazer com que o código seja bloqueante
- [x] Alternar entre a execução de corrotinas
</quiz>


<quiz>
Dizemos que um código é cooperativo quando:
- [x] Quando ele cede a vez para outro código ser executado
- [x] Quando ele usa a palavra reservada await
- [x] Quando ele permite ser escalonado
- [ ] Quando ele usa async def
</quiz>

<quiz>
Sobre o uso de await no código, podemos afirmar que:

```python hl_lines="8"
@pytest.mark.asyncio 
async def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username='alice', password='secret', email='teste@test'
        )
        session.add(new_user)
        await session.commit() 
```

- [x] Permite escalonamento durante a comunicação com o banco de dados
- [ ] Bloqueia a execução até que o commit seja concluído
- [ ] Cria uma nova corrotina
- [ ] Faz cooperação com o banco de dados
</quiz>


<quiz>
Qual a função do loop de eventos?
- [x] Gerenciar a execução de corrotinas de maneira ordenada
- [ ] Executar corrotinas simultaneamente
- [x] Escalonar entre código cooperativo
- [x] Tornar a execução não bloqueante
</quiz>

<quiz>
Qual a necessidade de usarmos `asyncio.run`?

```python
run(corrotina())
```

- [x] Executar tarefas não bloqueantes de forma bloqueante
- [ ] Bloquear o código durante execuções não bloqueantes
- [ ] Tonar a execução de funções síncronas em assíncronas
</quiz>

<quiz>
Qual a função do greenlet no projeto?
- [x] Permitir que o SQLAlchemy faça programação assíncrona
- [ ] Permitir que o coverage cubra funções async
- [ ] Substituir o asyncio
- [ ] Criar loops de eventos
</quiz>


<quiz>
Qual a função da flag `-k` no pytest?
- [x] Executar todos os testes com nomes correspondentes a flag
- [ ] Listar todos os testes que podem ser executados
- [ ] Matar (kill) todos os testes que não funcionarem
- [ ] Pausar a execução dos testes caso um falhe
</quiz>

<quiz>
Qual a função de `pytest_asyncio.fixture` no código?

```python
@pytest_asyncio.fixture
async def session():
    # ...
```

- [ ] Cria uma fixture bloqueante
- [ ] Cria uma fixture que só pode ser usada em testes assíncronos
- [x] Cria uma fixture executada pelo loop de eventos
</quiz>

<quiz>
Ao que se refere `expire_on_commit=False` na criação da sessão?

```python
async def get_session():
    async with AsyncSession(engine, expire_on_commit=False) as session: 
        yield session
```

- [ ] Expira os dados não commitados
- [x] Não limpa a sessão após o commit
- [ ] Cria uma sessão com tempo de vida
</quiz>


<quiz>
Adicionar `async def` ao código cria:
- [ ] Uma função assíncrona
- [x] Uma corrotina
- [ ] Um loop de eventos
- [ ] Um código bloqueante
</quiz>
