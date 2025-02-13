# Exercícios da aula 08

## Exercício 01

Reveja os endpoints criados por você em exercícios anteriores e adicione `#!python async` e `#!python await` para que eles se tornem não bloqueantes também.

### Solução

> TODO: Adicionar solução para o exercício 01

## Exercícios 02

Altere o endpoint `read_root` para suportar `asyncio`.

### Solução

```python title="fast_zero/app.py" hl_lines="2"
@app.get('/')
async def read_root():
    return {'message': 'Olá Mundo!'}
```
