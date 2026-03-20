lista = []

def adicionando_item_na_lista():
    nome = input("Digite o nome do item que deseja adicionar na lista")
    return lista.append(nome)

def removendo_item_da_lista():
    nome = input("Digite o nome do item que deseja remover: ")
    return lista.remove(nome)

def mostrando_itens_da_lista():
    for i in lista:
        print(i)
    
def gerenciador_de_tarefas(valor):
    match valor:
        case 1:
            print("Adicionar tarefa: ")
            adicionando_item_na_lista()
            print("Tarefa adicionado com sucesso!")
        case 2:
            print("Exibindo itens: ")
            mostrando_itens_da_lista()
        case 3:
            print("Remover tarefa: ")
            removendo_item_da_lista()
            print("Tarefa removida com sucesso!")
        case 0: 
            print("Saindo...")

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
            gerenciador_de_tarefas(1)
        elif teclado == '2':
            gerenciador_de_tarefas(2)
        elif teclado == '3':
            gerenciador_de_tarefas(3)
        else:
            gerenciador_de_tarefas(0)
            break
    while (resp := input('Deseja sair mesmo? [S/N] ').upper()) not in {'S', 'N'}:
        print('Valor INVÁLIDO!')
    if resp == 'S':
        break
