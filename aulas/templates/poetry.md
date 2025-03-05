	Para usarmos uma versão específica do python no nosso ambiente devemos pedir ao poetry que instale essa versão:

	```bash title="$ Execução no terminal!"
	poetry python install {{full_version}}  # (1)!
	```

	1. Essa era a maior versão do {{short_version}} quando escrevi

	Em conjunto com essa instrução, devemos dizer ao poetry que usaremos exatamente a versão `{{short_version}}` em nosso projeto. Para isso alteraremos o arquivo de configuração do projeto o `pyproject.toml` na raiz do projeto:

	```toml title="pyproject.toml" linenums="9"
	[project]
	# ...
	requires-python = ">={{short_version}},<4.0" # (1)!
	```

	1. Qualquer versão maior ou igual a {{short_version}} e menor que 4.0
