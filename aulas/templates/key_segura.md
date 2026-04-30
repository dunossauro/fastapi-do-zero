???+ example "Caso queira gerar sem sair da página da aula"
	Se quiser, você pode só criar no `run` aqui mesmo e receber uma secret aleatória:

	```pyodide
	import secrets
	print(secrets.token_hex(32))
	```
