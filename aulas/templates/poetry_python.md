	Para usarmos uma versão específica do python no nosso ambiente devemos pedir ao poetry que instale essa versão:

	```bash title="$ Execução no terminal!"
	poetry python install {{short_version}}  #(1)!
	```

	1. Instala a ultima release da versão {{short_version}} do python
	
	Uma mensagem como essa deve ser a resposta do comando anterior:
	
	```bash title="Resposta do comando `poetry python install`"
	Downloading and installing {{full_version}} (cpython) ... Done #(1)!
	Testing {{full_version}} (cpython) ... Done
	```
	
	1. {{full_version}} é ultima release da versão lançada enquanto esscrevia esse material.
