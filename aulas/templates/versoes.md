???+ danger "Sobre as verões das bibliotecas instaladas"
    ```python exec="on"
	from pathlib import Path
	from datetime import datetime
	target = Path('codigo_das_aulas/13/pyproject.toml')
    modified = target.stat().st_ctime
    print(f'A última atualização dos pacotes deste material foi feita em: **{datetime.fromtimestamp(modified).strftime("%d/%m/%Y às %H:%M")}**.Caso você esteja lendo este material em um futuro distante ou enfrente erros de instalação, o [apêndice C](/apendices/c_versoes_usadas/) contém todas as versões usadas no ambiente de forma detalhada.')
	```
