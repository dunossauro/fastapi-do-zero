	```docker title="Dockerfile"
	FROM python:{{short_version}}-slim
	WORKDIR app/
	COPY . .

	RUN pip install .

	EXPOSE 8000
	CMD uvicorn --host 0.0.0.0 fast_zero.app:app
	```

	Aqui está o que cada linha faz:

	1. `FROM python:{{short_version}}-slim`: define a imagem base para nosso contêiner. Estamos usando a versão slim da imagem do Python {{short_version}}, que tem tudo que precisamos para rodar nossa aplicação.
	2. `WORKDIR app/`: define o diretório em que executaremos os comandos a seguir.
	3. `COPY . .`: copia todos os arquivos do diretório atual para o contêiner.
	4. `RUN pip install .`: instala as dependências do nosso projeto. Somente as de `project.dependencies`, sem os grupos de opcionais.
	8. `EXPOSE 8000`: informa ao Docker que o contêiner escutará na porta 8000.
	9. `CMD uvicorn --host 0.0.0.0 fast_zero.app:app`: define o comando que será executado quando o contêiner for iniciado.
