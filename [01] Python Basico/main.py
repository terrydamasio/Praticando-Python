import os

# Implementar módulos e tratamento de erros.

usuario = dict()
cadastros = list()

def menu():
    print("="*21)
    print(" SISTEMA DE CLIENTES ")
    print("="*21)
    
    print("1 - Cadastrar cliente")    
    print("2 - Exibir clientes")    
    print("3 - Buscar clientes")    
    print("4 - Atualizar clientes")    
    print("5 - Excluir clientes")    
    print("6 - Sair")

def choise():   
    global cadastros
    print("-"*20)
    opcao = int(input("Digite uma opção: "))
    match (opcao):
        case 1:
            # Cadastrar cliente
            while True: 
                print("-"*20)
                usuario['nome'] = str(input("Nome: "))
                usuario['email'] = str(input("E-mail: "))
                usuario['cpf'] = str(input("CPF: "))
                usuario['telefone'] = str(input("Telefone: "))
                
                cadastros.append(usuario.copy())
                
                opcao = str(input("Deseja inserir mais usuários? [S/N] ")).upper()
                while opcao not in ("SN"):
                    print("Opção inválida! Tente novamente.")
                    opcao = str(input("Deseja inserir mais usuários? [S/N] ")).upper()
            
                if opcao in "N":    
                    main()
                    break
        case 2:
            # Exibir clientes
            print("-"*20)
            print("LISTA DE CLIENTES")
            print("-"*20)
            
            for c in cadastros:
                print(f"{cadastros.index(c) + 1} - {c['nome']}")
                  
            # Voltar ao menu
            print("-"*20)
            opcao = str(input("Digite 'M' para voltar menu: ")).upper()
            while opcao not in ("M"):
                    print("Opção inválida! Tente novamente.")
                    opcao = str(input("Digite 'M' para voltar menu: ")).upper()
            
            if opcao in "M":
                main()
        case 3: 
            # Buscar clientes
            print("-"*20)
            print("LISTA DE CLIENTES")
            print("-"*20)
            
            usuario_buscar = str(input("Usuario para buscar: ")).upper()
            for c in cadastros:
                if usuario_buscar in c['nome'].upper():
                    print(c['nome'])
            
            # Voltar ao menu
            opcao = str(input("Deseja inserir mais usuários? [S/N] ")).upper()
            while opcao not in ("SN"):
                print("Opção inválida! Tente novamente.")
                opcao = str(input("Deseja inserir mais usuários? [S/N] ")).upper()
            
                if opcao in "N":    
                    main()
                    break
        case 4: 
            # Atualizar clientes
            print("Atualizar clientes")
            
            # Voltar ao menu
            opcao = str(input("Digite 'M' para voltar menu: ")).upper()
            while opcao not in ("M"):
                    print("Opção inválida! Tente novamente.")
                    opcao = str(input("Digite 'M' para voltar menu: ")).upper()
            
            if opcao in "M":
                main()
        case 5: 
            # Excluir cliente
            print("Excluir clientes")
            
            # Voltar ao menu
            opcao = str(input("Digite 'M' para voltar menu: ")).upper()
            while opcao not in ("M"):
                    print("Opção inválida! Tente novamente.")
                    opcao = str(input("Digite 'M' para voltar menu: ")).upper()
            
            if opcao in "M":
                main()
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