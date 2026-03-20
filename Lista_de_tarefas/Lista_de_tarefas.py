lista = []

while True:
    print("Bem vindo ao gerenciador de tarefas diarias!!")
    print("-------------------------------------------")
    print("Digite [1] para adicionar um item na lista")
    print("Digite [2] para exibir os itens da lista")
    print("Digite [3] para remover um item da lista")
    print("Digite [0] para sair do programa")
    print("-------------------------------------------")
    
    while (teclado :=input("selecione uma opção: ")) not in {1,2,3,0}:
        if teclado == '1':
           nome = input("Adicionar tarefa: ")
           lista.append(nome)
           print("Tarefa adicionado com sucesso!")
        elif teclado == '2':
            print("Exibindo itens: ")
            for i in lista:
                print(i)
        elif teclado == '3':
            nome = input("Remover tarefa: ")
            lista.remove(nome)
            print("Tarefa removida com sucesso!")
        else:
            print("Saindo...")
            break
    while (resp := input('Deseja sair mesmo? [S/N] ').upper()) not in {'S', 'N'}:
        print('Valor INVÁLIDO!')
    if resp == 'S':
        break
