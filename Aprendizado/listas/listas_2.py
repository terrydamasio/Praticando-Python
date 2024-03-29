dados = list()
pessoas = list()

dados.append("Terry")
dados.append(20)
dados.append("Kerry")
dados.append(19)

# criando uma cópia de dados[] dentro de pessoas[] 
pessoas.append(dados[:])

# criando listas compostas
pessoas = [["Terry", 20], ["Kerry", 19], ["Júlia", 18], ["Ricardo", 19]]
print(pessoas)