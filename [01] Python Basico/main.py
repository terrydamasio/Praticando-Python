import os

# Fazer crud de cliente utilizando tuplas, lista, dicionario, funções, módulos e tratamento de erros.

usuario = dict()
cadastros = list()

def menu():
    print("1 - Cadastrar cliente")    
    print("2 - Exibir clientes")    
    print("3 - Buscar clientes")    
    print("4 - Atualizar clientes")    
    print("5 - Excluir clientes")    
    print("6 - Sair")

def choise():    
    opcao = int(input("Digite uma opção: "))
    match (opcao):
        case 1:
            # cadastrar cliente
        case 2:
            # exibir clientes
        case 3: 
            # buscar clientes
        case 4: 
            # Atualizar clientes
        case 5: 
            # Excluir cliente
        case 6:
            print("Saindo...")
        case __:
            print("Opção Inválida! Tente novamente")
            main()

def main():
    os.system('cls')
    menu()
    choise()

if __name__ == '__main__':
    main()