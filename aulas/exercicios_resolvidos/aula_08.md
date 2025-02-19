# Exercícios da aula 08

## Exercício 01

Reveja os endpoints criados por você em exercícios anteriores e adicione `#!python async` e `#!python await` para que eles se tornem não bloqueantes também.

### Solução

Para o exercício do endpoit que retorna o HTML, a resolução é bastante simples:

```python hl_lines="2"
@app.get('/exercicio-html', response_class=HTMLResponse)
async def exercicio_aula_02():
    return """
	# ...
```

Para o endpoint de GET via ID:

```python hl_lines="2 5"
@app.get('/users/{user_id}', response_model=UserPublic)
async def read_user__exercicio(
    user_id: int, session: Session = Depends(get_session)
):
    db_user = await session.scalar(select(User).where(User.id == user_id))

    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    return db_user
```

## Exercícios 02

Altere o endpoint `read_root` para suportar `asyncio`.

### Solução

```python title="fast_zero/app.py" hl_lines="2"
@app.get('/')
async def read_root():
    return {'message': 'Olá Mundo!'}
```
