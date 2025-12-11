# 11 - Dockerizando a nossa aplicação e introduzindo o PostgreSQL


<quiz>
Qual a função do arquivo `Dockerfile`?
- [ ] Definir a rede que o contêiner usará
- [x] Especificar as instruções necessárias para criar uma imagem Docker personalizada
- [ ] Gerenciar o armazenamento de dados dentro do contêiner
- [ ] Definir o nome do contêiner que será criado
</quiz>


<quiz>
Por que usamos a instrução `FROM python:3.11-slim` no dockerfile?
- [ ] Para criar uma imagem baseada no sistema operacional Windows
- [x] Para definir a imagem base do Docker como uma versão do Python 3.11
- [ ] Para instalar o Python 3.11 no contêiner diretamente
- [ ] Para baixar a versão mais recente do Python no repositório oficial
</quiz>


<quiz>
Qual a função do arquivo `compose.yaml`?
- [ ] Subir a aplicação de forma simples
- [x] Especificar os serviços e como eles se relacionam
- [ ] Substituir o Dockerfile
- [ ] Criar uma container docker
</quiz>

<quiz>
Qual instrução do Dockerfile o `entrypoint` substitui?
- [x] O comando de execução (CMD)
- [ ] A definição da imagem base (FROM)
- [ ] A exposição das portas (EXPOSE)
</quiz>

<quiz>
O que quer dizer escopo nas fixtures?
- [ ] Em quais testes elas vão atuar
- [ ] Se um módulo pode usar aquela fixture
- [x] Qual a duração da fixture
- [ ] Capturar as variáveis de ambiente
</quiz>

<quiz>
Por que usamos o escopo de "session" na fixture?
- [ ] Pra dizer que ela vai substituir a fixture de session
- [ ] Criar uma sessão do cliente com o banco de dados
- [ ] Dizer que a fixture tem a duração de um teste
- [x] Dizer que a fixture será executada uma única vez durante os testes
</quiz>

<quiz>
Para que serve o volume no docker?
- [ ] Para armazenar as imagens geradas
- [ ] Para adicionar um banco de dados
- [ ] Para armazenar o cache do docker
- [x] Para persistir arquivos na máquina host
</quiz>

<quiz>
O que faz a flag `-it` no CLI do docker?
- [ ] Conecta o container na internet
- [x] Roda o container no modo interativo
- [ ] Configura a rede do docker
- [ ] Passa as variáveis de ambiente
</quiz>

<quiz>
Por que precisamos usar o TestContainers no projeto?
- [ ] Para executar os testes dentro de containers
- [ ] Para testar os containers da aplicação
- [ ] Para criar imagens durante o teste
- [x] Para iniciar containers durante o teste
</quiz>


<quiz>
Qual a razão de termos instalado a biblioteca `psycopg` no projeto?
- [ ] Para permitir a conexão entre o banco de dados e o docker
- [ ] Para permitir a conexão com bancos de dados SQLite
- [ ] Para fornecer suporte a operações de arquivo no sistema
- [x] Para permitir a conexão com bancos de dados PostgreSQL no projeto
</quiz>
