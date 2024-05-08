# criar lista e dicionário
pessoa = dict()
pessoas = list()
soma_idade = 0

# ler nome, idade e sexo
while True:
    pessoa['nome'] = str(input("Nome: "))
    pessoa['sexo'] = str(input("Sexo: [M/F] ")).upper()
    while pessoa['sexo'] not in "MF":
        print("ERRO! Por favor, digite apenas M ou F.")
        pessoa['sexo'] = str(input("Sexo: [M/F] ")).upper()
    
    pessoa['idade']  = int(input("Idade: "))
    soma_idade += pessoa['idade']

    pessoas.append(pessoa.copy())
    
    opcao = str(input("Quer continuar? [S/N] ")).strip().upper()
    while opcao not in "SN":
        print("Erro! Por favor digite apenas S ou N.")
        opcao = str(input("Quer continuar? [S/N] ")).strip().upper()

    if opcao in "N":
        break

# guardar os dicionários em uma lista
print('='*30)
print(f"A) Ao todo temos {len(pessoas)} pessoas cadastradas.")

# média de idade 
media = soma_idade/len(pessoas)
print(f"B) A média de idade é de {media} anos.")

# lista das mulheres
print(f"C) As mulheres cadastradas foram: ", end='')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(f"{p['nome']}", end='')
    
# lista com idade acima da média
print(f"D) As pessoas que estão acima da média: ", end='')
for p in pessoas:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f"{k} => {v}", end='')
print("---FIM---")