# Variável para armazenar o saldo inicial
saldo = 1000.00  # Valor inicial da conta fictícia

# Função para consultar o saldo
def consultar_saldo():
    print(f"Seu saldo atual é: R${saldo:.2f}")

# Função para sacar dinheiro
def sacar_dinheiro():
    global saldo
    valor_saque = float(input("Digite o valor que deseja sacar: R$"))
    if valor_saque > saldo:
        print("Saldo insuficiente. Não é possível sacar o valor desejado.")
    else:
        saldo -= valor_saque
        print(f"Você sacou: R${valor_saque:.2f}")
        print(f"Saldo restante: R${saldo:.2f}")

# Função para depositar dinheiro
def depositar_dinheiro():
    global saldo
    valor_deposito = float(input("Digite o valor que deseja depositar: R$"))
    saldo += valor_deposito
    print(f"Você depositou: R${valor_deposito:.2f}")
    print(f"Saldo atual: R${saldo:.2f}")

# Função principal do caixa eletrônico
def caixa_eletronico():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Consultar Saldo")
        print("2 - Sacar Dinheiro")
        print("3 - Depositar Dinheiro")
        print("4 - Sair")

        opcao = input("Opção: ")

        if opcao == '1':
            consultar_saldo()
        elif opcao == '2':
            sacar_dinheiro()
        elif opcao == '3':
            depositar_dinheiro()
        elif opcao == '4':
            print("Obrigado por utilizar nosso caixa eletrônico. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Inicia o caixa eletrônico
caixa_eletronico()