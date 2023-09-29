valor = float(input("Digite um número positivo ou negativo: "))

if valor < 0:
    print("O número é negativo ")
elif valor == 0:
    print("O número é zero")
elif valor > 0:
    print("O número é positivo")