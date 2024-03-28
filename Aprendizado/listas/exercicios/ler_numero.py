# criar array
lista = []
maior = 0
menor = 0

# ler valores numéricos 
for i in range(0,5):
    lista.append(int(input(f"Digite um valor para a posição {i}: ")))
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]

# descobrir os valores e índices
print("="*30)
print(f"Você digitou os valores {lista}")

print(f"O maior valor digitado foi {maior} na posição ", end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f"{i}", end='')

print()

print(f"O menor valor digitado foi {menor} na posição ", end='')
for i, v in enumerate(lista):
    if v == menor: 
        print(f"{i}", end='')