# funcao leiaInt() que vai funcionar semelhante ao input.
# fazer validação para aceitar apenas valores numéricos.

def readInt(msg):
    status = False 
    value = 0

    while True:
        num = str(input(msg))
        if num.isnumeric():
            value = int(num)
            status = True
        else:
            print("\033[0;31mERRO! Digite um número inteiro válido.\033[m")
        if status:
            break
    return value

num = readInt("Digite um número: ")
print(f"Você acabou de digitar o número: {num}")
