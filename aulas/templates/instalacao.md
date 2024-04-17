	```shell title="$ Execução no terminal!"
	pyenv update
	pyenv install {{short_version}}:latest
	```

	??? bug "Para quem usa Windows"
		O pyenv-win tem um [bug intermitente](https://github.com/pyenv-win/pyenv-win/issues/407){:target="_blank"} em relação ao uso de `:latest`:

	    ```powershell
		PS C:\Users\vagrant> pyenv install {{short_version}}:latest
		:: [Info] ::  Mirror: https://www.python.org/ftp/python
		pyenv-install: definition not found: {{short_version}}:latest

	    See all available versions with `pyenv install --list`.
		Does the list seem out of date? Update it using `pyenv update`.
		```
		
		Caso você se depare com esse erro, pode rodar o comando `pyenv install --list` e ver a maior versão disponível do python no momento da sua instalação. Em seguida executar `pyenv install {{short_version}}.<a maior versão disponível>`. Nesse momento em que escrevo é a versão {{ full_version }} :

	    ```powershell
		PS C:\Users\vagrant> pyenv install {{full_version}}
		:: [Info] ::  Mirror: https://www.python.org/ftp/python
		:: [Downloading] ::  {{full_version}} ...
		:: [Downloading] ::  From https://www.python.org/ftp/python/{{full_version}}/{{full_version}}-amd64.exe
		:: [Downloading] ::  To   C:\Users\vagrant\.pyenv\pyenv-win\install_cache\python-{{full_version}}-amd64.exe
		:: [Installing] ::  {{full_version}} ...
		:: [Info] :: completed! {{full_version}}
		```

		Desta forma os próximos comandos podem ser executados normalmente.

	    Certifique que a versão do python {{short_version}} esteja instalada:


	```shell title="$ Execução no terminal!" hl_lines="6"
	pyenv versions
	* system (set by /home/dunossauro/.pyenv/version)
    3.10.12
	3.11.1
	3.12.0
	{{ full_version }}
	3.12.0b1
	```

	A resposta esperada é que o `Python {{ full_version }}` (a maior versão do python {{ short_version }} enquanto escrevia esse material) esteja nessa lista.
