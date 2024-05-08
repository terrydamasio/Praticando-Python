print("Contador")
print("-"*30)
param1 = int(input("Início: "))
param2 = int(input("Fim: ")) + 1
param3 = int(input("Passo: "))

def cont(i, f, p):
    for c in range(i, f, p):
        print(f"{c}, ", end='')

print(cont(param1, param2, param3))
