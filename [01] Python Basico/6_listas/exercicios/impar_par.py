numeros = list()
par = list()
impar = list()

# cadastrar os valores impares e pares separados
# mostrar os valores impares e pares em ordem crescente
for c in range(1, 8):
    numeros.append(int(input(f"Digite o {c}º valor: ")))
    
for numero in numeros:
    if numero % 2 == 0:
        par.append(numero)
    elif numero % 2 == 1:
        impar.append(numero)
        
par.sort()
impar.sort()
print(f"Os valores pares digitados foram: {par}")
print(f"Os valores ímpares digitados foram: {impar}")
