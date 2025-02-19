# 11 - Dockerizando a nossa aplicação e introduzindo o PostgreSQL


<?quiz?>
question: 01 - Qual a função do arquivo `compose.yaml`?
answer: Subir a aplicação de forma simples
answer-correct: Especificar os serviços e como eles se relacionam
answer: Substituir o Dockerfile
answer: Criar uma container docker
content:
<?/quiz?>

<?quiz?>
question: 02 - Qual instrução do Dockerfile o `entrypoint` substitui?
answer-correct: O comando de execução (CMD)
answer: A definição da imagem base (FROM)
answer: A exposição das portas (EXPOSE)
content:
<?/quiz?>

<?quiz?>
question: 03 - O que quer dizer escopo nas fixtures?
answer: Em quais testes elas vão atuar
answer: Se um módulo pode usar aquela fixture
answer-correct: Qual a duração da fixture
answer: Capturar as variáveis de ambiente
content:
<?/quiz?>

<?quiz?>
question: 04 - Por que usamos o escopo de "session" na fixture?
answer: Pra dizer que ela vai substituir a fixture de session
answer: Criar uma sessão do cliente com o banco de dados
answer: Dizer que a fixture tem a duração de um teste
answer-correct: Dizer que a fixture será executada uma única vez durante os testes
content:
<?/quiz?>

<?quiz?>
question: 05 - Para que serve o volume no docker?
answer: Para armazenar as imagens geradas
answer: Para adicionar um banco de dados
answer: Para armazenar o cache do docker
answer-correct: Para persistir arquivos na máquina host
content:
<?/quiz?>

<?quiz?>
question: 06 - O que faz a flag `-it` no CLI do docker?
answer: Conecta o container na internet
answer-correct: Roda o container no modo interativo
answer: Configura a rede do docker
answer: Passa as variáveis de ambiente
content:
<?/quiz?>

<?quiz?>
question: 07 - Por que precisamos usar o TestContainers no projeto?
answer: Para executar os testes dentro de containers
answer: Para testar os containers da aplicação
answer: Para criar imagens durante o teste
answer-correct: Para iniciar containers durante o teste
content:
<?/quiz?>
