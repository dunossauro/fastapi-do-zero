	```docker
	FROM python:{{short_version}}-slim
	ENV POETRY_VIRTUALENVS_CREATE=false

	WORKDIR app/
	COPY . .

	RUN pip install poetry

	RUN poetry config installer.max-workers 10
	RUN poetry install --no-interaction --no-ansi

	EXPOSE 8000
	CMD poetry run uvicorn --host 0.0.0.0 fast_zero.app:app
	```

	Aqui está o que cada linha faz:

	1. `FROM python:{{short_version}}-slim`: define a imagem base para nosso contêiner. Estamos usando a versão slim da imagem do Python {{short_version}}, que tem tudo que precisamos para rodar nossa aplicação.
	2. `ENV POETRY_VIRTUALENVS_CREATE=false`: define uma variável de ambiente que diz ao Poetry para não criar um ambiente virtual. (O container já é um ambiente isolado)
	3. `RUN pip install poetry`: instala o Poetry, nosso gerenciador de pacotes.
	4. `WORKDIR app/`: define o diretório em que executaremos os comandos a seguir.
	5. `COPY . .`: copia todos os arquivos do diretório atual para o contêiner.
	6. `RUN poetry config installer.max-workers 10`: configura o Poetry para usar até 10 workers ao instalar pacotes.
	7. `RUN poetry install --no-interaction --no-ansi`: instala as dependências do nosso projeto sem interação e sem cores no output.
	8. `EXPOSE 8000`: informa ao Docker que o contêiner escutará na porta 8000.
	9. `CMD poetry run uvicorn --host 0.0.0.0 fast_zero.app:app`: define o comando que será executado quando o contêiner for iniciado.
