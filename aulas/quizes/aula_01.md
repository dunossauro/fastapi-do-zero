# 01 - Configurando o Ambiente de Desenvolvimento

<quiz>
Qual a função do pipx?
- [ ] Criar e gerenciar ambientes virtuais para bibliotecas
- [x] Instalar bibliotecas isoladamente de forma global
- [ ] Uma alternativa ao pip
- [ ] Uma alternativa ao venv
</quiz>

<quiz>
Qual a função do Poetry?
- [ ] Uma alternativa ao pip
- [x] Gerenciar um projeto python
- [ ] Tem o mesmo propósito do pipx
</quiz>

<quiz>
O que faz o comando `fastapi dev`?
- [ ] Cria um ambiente de desenvolvimento para o FastAPI
- [ ] Inicia o servidor de produção do FastAPI
- [x] Inicia o Uvicorn em modo de desenvolvimento
- [ ] Instala o FastAPI
</quiz>

<quiz>
Ao que se refere o endereço `127.0.0.1`?
- [x] Ao endereço de rede local
- [x] Caminho de loopback
- [ ] Endereço do FastAPI
</quiz>

<quiz>
A flag do poetry `--group dev` instala os pacotes
- [ ] de produção
- [x] de desenvolvimento
- [ ] de testes
</quiz>

<quiz>
Qual a função do taskipy?
- [x] Criar "atalhos" para comandos mais simples
- [x] Facilitar o manuseio das operações de terminal
- [ ] Instalar ferramentas de desenvolvimento
- [ ] Gerenciar o ambiente virtual
</quiz>

<quiz>
O pytest é:
- [ ] um linter
- [ ] um formatador de código
- [x] framework de testes
</quiz>

<quiz>
Qual a ordem esperada de execução de um teste?
- [x] arrange, act, assert
- [ ] act, assert, arrange
- [ ] arrange, assert, act
</quiz>

<quiz>
Dentro do nosso teste, qual a função da chamada na linha em destaque?

```python hl_lines="4"
def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}
```
	
- [ ] assert
- [ ] arrange
- [x] act
</quiz>

<quiz>
Na cobertura de testes, o que quer dizer `Stmts`?
- [ ] Linha cobertas pelo teste
- [ ] Linhas não cobertas pelo teste
- [x] Linhas de código
</quiz>
