# cadastrar nome e peso de pessoas e colocar em uma lista
pessoa = list()
dados = list()

while True:
    pessoa.append(str(input("Nome: ")))
    pessoa.append(float(input("Peso: ")))
    if len(dados) == 0:
        maiPeso = menPeso = pessoa[1]
    else:
        if pessoa[1] > maiPeso:
            maiPeso = pessoa[1]
        if pessoa[1] < menPeso:
            menPeso = pessoa[1]

    dados.append(pessoa[:])
    pessoa.clear()

    opcao = str(input("Quer continuar? [S/N] ")).strip().upper()

    if opcao in 'N':
        break

print('\nCadastros')
print('='*30)
print(dados)

# listar as mais pesadas
# listar as mais leves
        
print(f"No total, você cadastrou {len(dados)} pessoa(s).")    
print(f"O maior peso foi de {maiPeso}Kg. Peso de ", end='')   
for p in dados:
    if p[1] == maiPeso:
        print(f"{p[0]}")
        
print(f"O maior peso foi de {menPeso}Kg. Peso de ", end='')
for p in dados:
    if p[1] == menPeso:
        print(f"{p[0]}")