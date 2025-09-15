# 12 - Automatizando os testes com Integração Contínua (CI)

<?quiz?>
question: 01 - Qual a função da integração contínua?
answer: Proibir que código que não funciona seja commitado
answer-correct: Verificar se a integração das alterações foi bem sucedida
answer: Impedir que pessoas de fora integrem código em nosso repositório
answer: Integrar novos commits ao repositório
content:

A integração contínua tem como objetivo garantir que as mudanças feitas no código sejam integradas de maneira contínua e automatizada, verificando se não houve falhas nas integrações e garantindo a funcionalidade do código no repositório.
<?/quiz?>


<?quiz?>
question: 02 - O que é o Github Actions?
answer: Uma aplicação que executa os testes localmente
answer: Um test runner como o pytest
answer: Forma de integrar o github com outras aplicações
answer-correct: Um serviço do github para CI
content:
O GitHub Actions é um serviço oferecido pelo GitHub para automatizar fluxos de trabalho de integração contínua e entrega contínua (CI/CD) diretamente no repositório do GitHub.
<?/quiz?>


<?quiz?>
question: 03 - O que é um workflow de CI?
answer-correct: Uma lista de passos que o CI deve executar
answer-correct: Uma automação executada sempre código é adicionado ao respositório
answer: Uma forma de versionar software como o git
answer: Passos que serão executados antes do commit
content:
Um workflow de CI é uma sequência de passos automáticos definidos em um arquivo YAML, que são executados sempre que mudanças no código são enviadas para o repositório, garantindo que o código esteja sempre em funcionamento.
<?/quiz?>


<?quiz?>
question: 04 - Quando o nosso trigger de CI é ativado?
answer-correct: Sempre que fazemos um push
answer-correct: Sempre que criamos um pull request
answer: Sempre que um commit é feito
answer: Sempre que uma issue é aberta
content:
O trigger de CI é ativado por eventos como push e pull request, que indicam que mudanças no código foram feitas e precisam ser verificadas automaticamente.
<?/quiz?>


<?quiz?>
question: 05 - Nos steps, o que quer dizer "uses"?
answer-correct: Diz que vamos usar uma action pronta
answer: Diz que vamos executar uma instrução de shell
answer: Que vamos fazer a instalação de um componente no workflow
answer: Fazer checkout do código do repositório
content:
Quando usamos "uses" em um step, estamos referenciando uma action já pronta, geralmente fornecida pela comunidade ou pelo próprio GitHub, para ser executada automaticamente no workflow.
<?/quiz?>


<?quiz?>
question: 06 - Nos steps, o que quer dizer "run"?
answer: Que vamos usar uma action pronta do github
answer: Serve para dizer que vamos usar um passo
answer: Definir uma variável de ambiente
answer-correct: Diz que vamos executar uma instrução de shell
content:
O comando "run" permite executar comandos ou instruções diretamente no sistema operacional do ambiente de CI, como comandos de shell, scripts ou outras tarefas programadas.
<?/quiz?>


<?quiz?>
question: 07 - Qual a função das "secrets" no arquivo yaml?
answer: Criar variáveis de ambiente
answer-correct: Não expor dados sensíveis no arquivo de ci
answer: Substituir variáveis ​​com valores dinâmicos
answer: Organizar o código YAML
content:
As "secrets" no GitHub Actions são usadas para armazenar informações sensíveis, como senhas ou chaves de API, de maneira segura, sem expô-las diretamente no arquivo YAML.
<?/quiz?>


<?quiz?>
question: 08 - O que faz o comando "gh secret set"?
answer: Ele adiciona um novo repositório ao GitHub.
answer-correct: Ele define um segredo no GitHub para ser usado em GitHub Actions.
answer: Ele atualiza o repositório com novas permissões de acesso.
answer: Ele cria um novo repositório no GitHub.
content:
O comando "gh secret set" é utilizado para criar e definir segredos no repositório GitHub, que podem ser utilizados no GitHub Actions para ações que requerem dados sensíveis.
<?/quiz?>


<?quiz?>
question: 09 - O que deve ser declarado na chave "env" do arquivo de pipeline?
answer: O nome do repositório.
answer-correct: Variáveis de ambiente que serão utilizadas no pipeline.
answer: O nome dos branches no repositório.
answer: Os usuários que têm acesso ao repositório.
content:
A chave "env" define variáveis de ambiente no pipeline, as quais serão utilizadas durante a execução do workflow para armazenar valores dinâmicos e facilitar o processo de automação.
<?/quiz?>


<?quiz?>
question: 10 - O que deve ser declarado na chave "runs-on" do arquivo de pipeline?
answer: O número de jobs que serão executados.
answer-correct: O sistema operacional ou ambiente onde o workflow será executado.
answer: O nome do repositório de onde o código será puxado.
answer: O nome do serviço de CI/CD que irá rodar o pipeline.
content:
A chave "runs-on" especifica o ambiente ou sistema operacional onde o workflow será executado, como Ubuntu, Windows ou macOS.
<?/quiz?>

