# A - Instalando as ferramentas externas

{% include "templates/versoes.md" %}

Durante as aulas síncronas, diversas dúvidas sobre a configuração e instalação das ferramentas fora do python foram levantadas. A ideia dessa página é te auxiliar nas instalações.

São comandos rápidos e simples, não tenho a intensão de explicar o que essas ferramentas fazem exatamente, muitas explicações já foram escritas sobre elas na [página de configuração do projeto](../01.md){:target="_blank"}. A ideia é agrupar todas as instalações um único lugar.

## pipx

O pipx é uma ferramenta para simplificar a instalação de pacotes globais.

Para isso, você pode executar:

```shell title="$ Execução no terminal!"
pip install pipx
```

???+ warning "Instalação do pipx"
    Embora seja possível instalar via pip, em algumas versões é exigido o escopo de usuário `--user` para fazer a instalação global.
	
	A melhor forma de instalar o pipx ainda é usando o seu sistema operacional. Você pode consultar a documentação sobre como fazer isso. [documentação](https://pipx.pypa.io/stable/installation/)

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
