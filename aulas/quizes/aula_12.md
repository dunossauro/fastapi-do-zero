# 12 - Automatizando os testes com Integração Contínua (CI)

<?quiz?>
question: 01 - Qual a função da integração contínua?
answer: Proibir que código que não funciona seja commitado
answer-correct: Verificar se a integração das alterações foi bem sucedida
answer: Impedir que pessoas de fora integrem código em nosso repositório
answer: Integrar novos commits ao repositório
content:
<?/quiz?>

<?quiz?>
question: 02 - O que é o Github Actions?
answer: Uma aplicação que executa os testes localmente
answer: Um test runner como o pytest
answer: Forma de integrar o github com outras aplicações
answer-correct: Um serviço do github para CI
content:
<?/quiz?>

<?quiz?>
question: 03 - O que é um workflow de CI?
answer-correct: Uma lista de passos que o CI deve executar
answer-correct: Uma automação executada sempre código é adicionado ao respositório
answer: Uma forma de versionar software como o git
answer: Passos que serão executados antes do commit
content:
<?/quiz?>

<?quiz?>
question: 04 - Quando o nosso trigger de CI é ativado?
answer-correct: Sempre que fazemos um push
answer-correct: Sempre que criamos um pull request
answer: Sempre que um commit é feito
answer: Sempre que uma issue é aberta
content:
<?/quiz?>

<?quiz?>
question: 05 - Nos steps, o que quer dizer "uses"?
answer-correct: Diz que vamos usar uma action pronta
answer: Diz que vamos executar uma instrução de shell
answer: Que vamos fazer a instalação de um componente no workflow
answer: Fazer checkout do código do repositório
content:
<?/quiz?>

<?quiz?>
question: 06 - Nos steps, o que quer dizer "run"?
answer: Que vamos usar uma action pronta do github
answer: Serve para dizer que vamos usar um passo
answer: Definir uma variável de ambiente
answer-correct: Diz que vamos executar uma instrução de shell
content:
<?/quiz?>

<?quiz?>
question: 07 - Qual a função das "secrets" no arquivo yaml?
answer: Criar variáveis de ambiente
answer-correct: Não expor dados sensíveis no arquivo de ci
answer: Substituir variáveis ​​com valores dinâmicos
answer: Organizar o código YAML
content:
<?/quiz?>
