num1 = int(input("Digite um valor: "))
num2 = int(input("Digite outro valor: "))
opcao = 0

while opcao != 5:
    print('''Menu
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Sair do programa''')
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        soma = num1 + num2
        print(f"A soma entre {num1} e {num2} é {soma}.")
    elif opcao == 2:
        produto = num1 * num2
        print(f"O produto entre {num1} e {num2} é {produto}.")
    elif opcao == 3:
        if num1 > num2: 
            maior = num1
        else: 
            maior = num2
        print(f"O maior valor entre {num1} e {num2} é {maior}")
    elif opcao == 4:
        print("Informe os números novamente: ")
        num1 = float(input("Digite um valor: "))
        num2 = float(input("Digite outro valor: "))
    elif opcao == 5:
        print("Finalizando...")
    else:
        print("Opção inválida. Tente novamente!")

print("Fim do programa!")

