# 12 - Automatizando os testes com Integração Contínua (CI)

<quiz>
Qual a função da integração contínua?
- [ ] Proibir que código que não funciona seja commitado
- [x] Verificar se a integração das alterações foi bem sucedida
- [ ] Impedir que pessoas de fora integrem código em nosso repositório
- [ ] Integrar novos commits ao repositório

A integração contínua tem como objetivo garantir que as mudanças feitas no código sejam integradas de maneira contínua e automatizada, verificando se não houve falhas nas integrações e garantindo a funcionalidade do código no repositório.
</quiz>


<quiz>
O que é o Github Actions?
- [ ] Uma aplicação que executa os testes localmente
- [ ] Um test runner como o pytest
- [ ] Forma de integrar o github com outras aplicações
- [x] Um serviço do github para CI

O GitHub Actions é um serviço oferecido pelo GitHub para automatizar fluxos de trabalho de integração contínua e entrega contínua (CI/CD) diretamente no repositório do GitHub.
</quiz>


<quiz>
O que é um workflow de CI?
- [x] Uma lista de passos que o CI deve executar
- [x] Uma automação executada sempre código é adicionado ao respositório
- [ ] Uma forma de versionar software como o git
- [ ] Passos que serão executados antes do commit

Um workflow de CI é uma sequência de passos automáticos definidos em um arquivo YAML, que são executados sempre que mudanças no código são enviadas para o repositório, garantindo que o código esteja sempre em funcionamento.
</quiz>


<quiz>
Quando o nosso trigger de CI é ativado?
- [x] Sempre que fazemos um push
- [x] Sempre que criamos um pull request
- [ ] Sempre que um commit é feito
- [ ] Sempre que uma issue é aberta

O trigger de CI é ativado por eventos como push e pull request, que indicam que mudanças no código foram feitas e precisam ser verificadas automaticamente.
</quiz>


<quiz>
Nos steps, o que quer dizer `uses`?
- [x] Diz que vamos usar uma action pronta
- [ ] Diz que vamos executar uma instrução de shell
- [ ] Que vamos fazer a instalação de um componente no workflow
- [ ] Fazer checkout do código do repositório

Quando usamos "uses" em um step, estamos referenciando uma action já pronta, geralmente fornecida pela comunidade ou pelo próprio GitHub, para ser executada automaticamente no workflow.
</quiz>


<quiz>
Nos steps, o que quer dizer `run`?
- [ ] Que vamos usar uma action pronta do github
- [ ] Serve para dizer que vamos usar um passo
- [ ] Definir uma variável de ambiente
- [x] Diz que vamos executar uma instrução de shell

O comando "run" permite executar comandos ou instruções diretamente no sistema operacional do ambiente de CI, como comandos de shell, scripts ou outras tarefas programadas.
</quiz>


<quiz>
Qual a função das `secrets` no arquivo yaml?
- [ ] Criar variáveis de ambiente
- [x] Não expor dados sensíveis no arquivo de ci
- [ ] Substituir variáveis ​​com valores dinâmicos
- [ ] Organizar o código YAML

As "secrets" no GitHub Actions são usadas para armazenar informações sensíveis, como senhas ou chaves de API, de maneira segura, sem expô-las diretamente no arquivo YAML.
</quiz>


<quiz>
O que faz o comando `gh secret set`?
- [ ] Ele adiciona um novo repositório ao GitHub.
- [x] Ele define um segredo no GitHub para ser usado em GitHub Actions.
- [ ] Ele atualiza o repositório com novas permissões de acesso.
- [ ] Ele cria um novo repositório no GitHub.

O comando "gh secret set" é utilizado para criar e definir segredos no repositório GitHub, que podem ser utilizados no GitHub Actions para ações que requerem dados sensíveis.
</quiz>


<quiz>
O que deve ser declarado na chave `env` do arquivo de pipeline?
- [ ] O nome do repositório.
- [x] Variáveis de ambiente que serão utilizadas no pipeline.
- [ ] O nome dos branches no repositório.
- [ ] Os usuários que têm acesso ao repositório.

A chave "env" define variáveis de ambiente no pipeline, as quais serão utilizadas durante a execução do workflow para armazenar valores dinâmicos e facilitar o processo de automação.
</quiz>


<quiz>
O que deve ser declarado na chave `runs-on` do arquivo de pipeline?
- [ ] O número de jobs que serão executados.
- [x] O sistema operacional ou ambiente onde o workflow será executado.
- [ ] O nome do repositório de onde o código será puxado.
- [ ] O nome do serviço de CI/CD que irá rodar o pipeline.

A chave "runs-on" especifica o ambiente ou sistema operacional onde o workflow será executado, como Ubuntu, Windows ou macOS.
</quiz>

