dados = []

dados.append(str(input("Insira o seu nome: ")))
dados.append(int(input("Insira sua idade: ")))
dados.append(float(input("Insira sua altura: ")))

# percorrendo lista 
for indice, valor in enumerate(dados):
    print(f"No índice {indice} o valor é {valor} ")
print("-"*30)