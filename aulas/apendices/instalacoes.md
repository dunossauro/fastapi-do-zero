# A - Instalando as ferramentas externas

Durante as aulas síncronas, diversas dúvidas sobre a configuração e instalação das ferramentas fora do python foram levantadas. A ideia dessa página é te auxiliar nas instalações.

São comandos rápidos e simples, não tenho a intensão de explicar o que essas ferramentas fazem exatamente, muitas explicações já foram escritas sobre elas na [página de configuração do projeto](/01/#instalacao-do-python){:target="_blank"}. A ideia é agrupar todas as instalações um único lugar.

## Pyenv no Windows
Para instalar o pyenv você precisa abrir seu terminal como administrado e executar o comando:

```powershell
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
```

A mensagem `pyenv-win is successfully installed. You may need to close and reopen your terminal before using it.` aparecerá na tela. Dizendo que precisamos reinicar o shell. 

Só precisamos fechá-lo e abrir de novo.

## Pyenv no Linux/MacOS

Como não tenho como cobrir a instalação em todos as distros, vou usar uma ferramenta chamada pyenv-installer. É bastante simples, somente executar o comando:

```shell title="$ Execução no terminal!"
curl https://pyenv.run | bash
```

Após isso é importante que você siga a instrução de adicionar a configuração no seu `.bashrc`:

```bash title="~/.bashrc"
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
```

> Caso use zsh, xonsh, .... bom... Você deve saber o que está fazendo :)

Após isso reinicie o shell para que a variável de ambiente seja carregada.

??? warning "Caso esteja no ubuntu"
	É importante que você instale o `curl` e o `git` antes:
	
	```shell title="$ Execução no terminal!"
	sudo apt update
	sudo apt install curl git
	```

## Instalação do Python via pyenv

Agora, com o pyenv instalado, você pode instalar a versão do python que usaremos no curso. Como descrito na [página de configuração do projeto](/01/#instalacao-do-python){:target="_blank"}:

```shell title="$ Execução no terminal!"
pyenv install 3.12.3
```

A seguinte mensagem deve aparecer na tela:

```{.powershell .no-copy}
:: [Info] ::  Mirror: https://www.python.org/ftp/python
:: [Downloading] ::  3.12.3 ...
:: [Downloading] ::  From https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe
:: [Downloading] ::  To   C:\Users\vagrant\.pyenv\pyenv-win\install_cache\python-3.12.3-amd64.exe
:: [Installing] ::  3.12.3 ...
:: [Info] :: completed! 3.12.3
```

#### Configurando a versão no pyenv

Agora com versão instalada, devemos dizer ao shim, qual versão será usada globalmente. Podemos executar esse comando:

```shell title="$ Execução no terminal!"
pyenv global 3.12.3
```

Esse comando não costuma exibir nenhuma mensagem em caso de sucesso, se nada foi retornado, significa que tudo ocorreu como esperado.

Para testar se a versão foi definida, podemos chamar o python no terminal:

```shell title="$ Execução no terminal!"
python --version
Python 3.12.3 #(1)!
```

1. Responde que a versão correta foi setada!

## pipx

O pipx é uma ferramenta opcional na configuração do ambiente, mas é extremamente recomendado que você a instale para simplificar a instalação de pacotes globais.

Para isso, você pode executar:

```shell title="$ Execução no terminal!"
pip install pipx
```

A resposta do comando deverá ser parecida com essa:

```{.powershell .no-copy}
Collecting pipx
  Downloading pipx-1.6.0-py3-none-any.whl.metadata (18 kB)
Collecting argcomplete>=1.9.4 (from pipx)
  Downloading argcomplete-3.3.0-py3-none-any.whl.metadata (16 kB)
Collecting colorama>=0.4.4 (from pipx)
  Downloading colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Collecting packaging>=20 (from pipx)
  Downloading packaging-24.1-py3-none-any.whl.metadata (3.2 kB)
Collecting platformdirs>=2.1 (from pipx)
  Downloading platformdirs-4.2.2-py3-none-any.whl.metadata (11 kB)
Collecting userpath!=1.9,>=1.6 (from pipx)
  Downloading userpath-1.9.2-py3-none-any.whl.metadata (3.0 kB)
Collecting click (from userpath!=1.9,>=1.6->pipx)
  Downloading click-8.1.7-py3-none-any.whl.metadata (3.0 kB)
Downloading pipx-1.6.0-py3-none-any.whl (77 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 77.8/77.8 kB 2.2 MB/s eta 0:00:00
Downloading argcomplete-3.3.0-py3-none-any.whl (42 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 42.6/42.6 kB ? eta 0:00:00
Downloading colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Downloading packaging-24.1-py3-none-any.whl (53 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 54.0/54.0 kB ? eta 0:00:00
Downloading platformdirs-4.2.2-py3-none-any.whl (18 kB)
Downloading userpath-1.9.2-py3-none-any.whl (9.1 kB)
Downloading click-8.1.7-py3-none-any.whl (97 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 97.9/97.9 kB 295.3 kB/s eta 0:00:00
Installing collected packages: platformdirs, packaging, colorama, argcomplete, click, userpath, pipx
Successfully installed argcomplete-3.3.0 click-8.1.7 colorama-0.4.6 packaging-24.1 pipx-1.6.0 platformdirs-4.2.2 userpath-1.9.2
```

Para testar se o pipx foi instalado com sucesso, podemos executar:

```shell title="$ Execução no terminal!"
pipx --version
```

Se a versão for respondida, tudo está certo :)

Uma coisa recomendada de fazer, é adicionar os paths do pipx nas variáveis de ambiente, para isso podemos executar:

```shell title="$ Execução no terminal!"
pipx ensurepath
```

Dessa forma, os pacotes estarão no path. Podendo ser chamados pelo terminal sem problemas. A última coisa que precisa ser feita é abrir o terminal novamente, para que as novas variáveis de ambiente sejam lidas.

## ignr

Com o pipx você pode executar:

```shell title="$ Execução no terminal!"
pipx install ignr
```

## poetry

Com o pipx você pode executar:

```shell title="$ Execução no terminal!"
pipx install poetry
```

## GH

Gh é um CLI para o github. Facilita em diversos momentos.

A instalação para diversos sistemas e variantes pode ser encontrada [aqui](https://github.com/cli/cli#installation){:target="_blank"}.

## Docker

A instalação do docker é bastante diferente para sistemas operacionais diferentes e até mesmo em arquiteturas de processadores diferentes. Por exemplo, MacOS com intel ou arm, ou windows com WSL, ou hyper-V.

Por esse motivo, acredito que seja interessante você seguir os tutoriais oficiais:

- [Linux](https://docs.docker.com/desktop/install/linux-install/){:target="_blank"}
- [Windows](https://docs.docker.com/desktop/install/windows-install/){:target="_blank"}
- [MacOS](https://docs.docker.com/desktop/install/mac-install/){:target="_blank"}

### Docker Compose

A instalação varia bastante de sistema para sistema, mas você pode olhar o [guia de instalação oficial](https://docs.docker.com/compose/install/){:target="_blank"}.

## Git

O git pode ser baixado no [site oficial](https://git-scm.com/downloads){:target="_blank"} para windows e mac. No Linux acredito que todas as distribuições têm o `git` como um pacote disponível para instalação.
