# criando lista pequena
pessoa = list() 

# atribuindo valores
pessoa.append(str(input("Nome: "))) 
pessoa.append(int(input("Idade: ")))

# criando lista grande
dados = list() 

# criando cópia da lista pequena na grande
dados.append(pessoa[:])

# adicionando novos valores
pessoa[0] = str(input("Nome da mãe: "))
pessoa[1] = int(input("Idade: "))
dados.append(pessoa[:])

print("Cadastro de usuários")
print("="*30)

for nome, idade in dados:
    print(f"Nome: {nome}\nIdade: {idade}")
    print("-"*30)