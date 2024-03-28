# ler 4 valores e guardar em uma tupla
num = (
       int(input("Digite um valor: ")), 
       int(input("Digite outro valor: ")), 
       int(input("Digite mais um valor: ")), 
       int(input("Digite o último valor: "))
       )

# quantas vezes apareceu o valor 9
if 9 in num:
    print(f"O número 9 apareceu {num.count(9)} vez(es).")
    print("-"*30)

# posisão foi digitado o primeiro valor 3
if 3 in num:
    print(f"O número 3 está na {num.index(3)+1}º posição.")
    print("-"*30)

# quais foram os números pares
print("Os valores pares são: ")
for n in num:
    if n % 2 ==0:
        print(n, end=" ")