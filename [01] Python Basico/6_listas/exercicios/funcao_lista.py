lista_num = list()
par = list()

for c in range(1, 6):
    lista_num.append(int(input(f"Digite o {c}º valor: ")))

def listaPares(lista):
    for num in lista_num:
        if num % 2 == 0:
            par.append(num)
            
    print(f"O número números pares são: {par}.")

listaPares(lista_num)
