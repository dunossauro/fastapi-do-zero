	Para que a versão do python que instalamos via pyenv seja usada em nosso projeto criado com poetry, devemos dizer ao pyenv qual versão do python será usada nesse diretório:

	```shell title="$ Execução no terminal!"
	pyenv local {{full_version}}  # (1)!
	```

	1. Essa era a maior versão do {{short_version}} quando escrevi

	Esse comando criará um arquivo oculto chamado `.python-version` na raiz do nosso projeto:

	```title=".python-version"
	{{full_version}}
	```

	Esse arquivo fará com que toda vez que o terminal for aberto nesse diretório, o pyenv use a versão descrita no arquivo quando o python interpretador for chamado.

	Em conjunto com essa instrução, devemos dizer ao poetry que usaremos exatamente a versão `{{short_version}}` em nosso projeto. Para isso alteraremos o arquivo de configuração do projeto o `pyproject.toml` na raiz do projeto:

	```toml title="pyproject.toml" linenums="9"
	[tool.poetry.dependencies]
	python = "{{short_version}}.*"  # (1)!
	```

	1. `.*` quer dizer qualquer versão da {{short_version}}
