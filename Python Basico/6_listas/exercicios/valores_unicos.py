lista = []

while True:
    valor = int(input("Digite o um valor: "))
    if valor not in lista:
        lista.append(valor)
        print("Valor adicionado com sucesso!")
    else:
        print("Esse valor já existe.")
    
    opcao = str(input("Deseja continuar: [S/N] ")).strip().upper()
    if opcao in 'N':
        print("-"*30)
        print(f"Os valores digitados foram: {lista}")
        print("Finalizando programa...")
        break