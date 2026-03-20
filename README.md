## Exercicio de paradigma

# Descrição do problema escolhido
  programa simples de lista de tarefas via terminal com o intuito de ser interativo com loop infinito e inputs para o usuario digitar o que quiser e não se perder, visando as limitações de cada paradigma selecionado, bem como a linguagem.

# Paradigmas utilizados e suas características
  Os paradigmas usados foram: Orientado a objetos, que organiza o programa em objetos com atributos e métodos; e o Imperativo, que faz uma corrente de comandos sequenciais para o programa percorrer.

# Códigos desenvolvidos (duas versões)
os códigos estão devidamente separados em 2 pastas diferentes.
Na pasta "Lista_de_tarefas" encontra-se o código python do programa.
Na pasta "ListaDeTarefas" encontra-se o código java.

# Identificação do paradigma em cada código
Na pasta "Lista_de_tarefas" encontra-se o código python do programa. Organizado e pensado no modo Imperativo. Feito em um unico bloco massivo de passos sequenciais para o programa seguir.
Enquanto na pasta "ListaDeTarefas" encontra-se o código java do programa. Organizado e pensado no modo Orientação a objetos. Dividindo entre Main, com o codigo interativo que instancia o objeto e puxa seus metodos para serem utilizados a depender da escolha do usuario, e Tarefas que é a classe molde de objeto utilizado para o exercicio, bem simples com atributos, construtor e metodos claros.

# Comparação entre as abordagens
Apesar da verbosidade e tamanho de arquivo de java, a organização entre pastas/classes deixa tudo mais compreensivel e simples. No codigo em java existe apenas a Main e Tarefas. A Main identificamos a instancia do objeto e o loop principal que faz o programa rodar. utilizei um while e switch case para chamar os metodos dentro de Tarefas. Nisso, o atributo 'nome' era exigido na interação com o usuario e imediatamente jogado em uma lista dentro da classe. Com isso, o usuario pode adicionar quantos nomes quiser, ver a lista e remover um item da lista passando o mesmo nome. Um CRUD quase completo, pois nao vi a necessidade de incluir alteração.
já o código em python segue a mesma lógica, porem, visando a diferença de paradigma, não inclui o uso de Funções e foi utilizados 3 whiles para ter a mesma experiencia que a de java. o Código começa criando uma lista vazia e logo entra-se no primeiro loop while que é o inicio e demonstração das teclas em varios prints. o segundo loop inicia perguntando qual deseja apertar dentro o numero finito de opções. as escolhas são iguais, seguindo as mesmas logicas. o loop continua até apertar qualquer outra tecla das que não estão listadas, assim o terceito loop entra para perguntar se deseja mesmo sair. caso digite 's', o terceiro loop quebra os dois em andamento, finalizando o programa. caso, contrario ao 's', ele reinicia do loop mais externo.
A necessidade de utilizar esses 3 whiles foi bem dificil de planejar e executar, tendo em vista q no java o uso do switch reinicia o loop, em python a coisa foi mais manual e dificultosa.

# Reflexão final

O exercicio mostrou na prática que independente do método, linguagem e sintax um programa/problema pode ser abordado por maneiras diferentes, bem como pensar diferentes, e chegar numa resolução em comum e única para tal pedido.
Acredito que para um proposito tão simples como esse programa se dispos, a linguagem em python com o metodo imperativo foi o mais efetivo, principalmente pelo tamanho em arquivo e locação de memoria.. Claro que uma abordagem maior e com varios usuarios usanndo em web seria bastante diferente, porem no atual estado, python tem o seu brilho.
No fim, como falei no ponto anterior, o exercicio deixa bem claro as diferenças entre linguaguens e métodos abordados, mesmo tendo um programa com as mesmas telas e funcionalidades.







