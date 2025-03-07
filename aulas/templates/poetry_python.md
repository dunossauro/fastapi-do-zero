	Para utilizarmos uma versão específica do Python em nosso ambiente, devemos solicitar ao Poetry que instale essa versão:
	```bash title="$ Execução no terminal!"
	poetry python install {{short_version}}  #(1)!
	```

	1. Instala a última release da versão {{short_version}} do python
	
	Uma resposta similar a esta deve ser retornada ao executar o comando:
	
	```bash title="Resposta do comando `poetry python install`"
	Downloading and installing {{full_version}} (cpython) ... Done #(1)!
	Testing {{full_version}} (cpython) ... Done
	```
	
	1. {{full_version}} é a última release da versão lançada enquanto esscrevia esse material.
