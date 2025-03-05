    ```shell title="$ Execução no terminal!"
    poetry env use {{short_version}}
    ```

	Em conjunto com essa instrução, devemos dizer ao poetry que usaremos exatamente a versão `{{short_version}}` em nosso projeto. Para isso alteraremos o arquivo de configuração do projeto o `pyproject.toml` na raiz do projeto:

	```toml title="pyproject.toml" linenums="9"
	[project]
	# ...
	requires-python = ">={{short_version}},<4.0" # (1)!
	```

	1. Qualquer versão maior ou igual a {{short_version}} e menor que 4.0
