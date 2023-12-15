# MODIFICAÇÕES

## Primeiro Commit
No primeiro commit do programa, foi implementada a lógica geral de programação do bot. Ele realizava as atualizações de informações recebidas e, com essas atualizações, 
o bot filtrava o comando emitido pelo usuário, passando por vários tratamentos de `if` e `elif` até construir a mensagem de retorno.

## Segundo Commit (Atual)
No Segundo commit, o bot não apenas realiza a lógica geral da programação, mas também recebe a mensagem, verifica se é a primeira interação com o bot para determinar se é 
necessário exibir uma mensagem de boas-vindas. Isso é feito por meio de salvamento e registro em um arquivo JSON. Além disso, a programação foi otimizada, removendo o excesso 
de `if` e `elif` e adicionando uma lógica de dicionário. Foram implementados também vários `prints` no código para que o terminal informe quais funções estão sendo 
executadas durante as interações com o usuário.

## Observações, Resoluções Futuras, Recomendações, etc.
Durante o funcionamento do código, percebeu-se um problema relacionado à dificuldade de encerrá-lo, exigindo o fechamento do terminal. Para resolver isso, 
pretende-se liberar o terminal e implementar uma maneira de encerrar o programa por meio de um comando no terminal.
