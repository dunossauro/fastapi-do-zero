    ```shell title="$ Execução no terminal!"
    poetry env use {{short_version}}
    ```

	Em conjunto com essa instrução, devemos também especificar no Poetry que usaremos exatamente a versão `{{short_version}}` em nosso projeto. Para isso, alteramos o arquivo de configuração pyproject.toml na raiz do projeto:

	```toml title="pyproject.toml" linenums="9"
	[project]
	# ...
	requires-python = ">={{short_version}},<4.0" # (1)!
	```

	1. A expressão `">={{short_version}},<4.0"` significa que qualquer versão maior ou igual a `{{short_version}}` e menor que 4.0 será válida para o projeto.
