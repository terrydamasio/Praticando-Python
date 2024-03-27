num = int(input("Digite um número para calcular o fatorial: "))
contador = num
fatorial = 1

while contador > 0:
    print(f"{contador}", end=' ')
    print(" x " if contador > 1 else " = ", end=' ')
    fatorial = fatorial * contador
    contador -= 1
print(f"O fatorial de {num} é {fatorial}")