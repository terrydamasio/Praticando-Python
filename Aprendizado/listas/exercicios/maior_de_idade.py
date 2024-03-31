# criar listas 
pessoa = list()
dados = list()
totMaior = totMenor = 0

# ler os dados e jogar dentro da lista maior
for c in range(0, 3):
    pessoa.append(str(input("Nome: ")))
    pessoa.append(int(input("Idade: ")))
    print('-'*20)
    dados.append(pessoa[:])
    # limpar dados de pessoa
    pessoa.clear() 

# verifica se pessoa é maior ou menor
for p in dados:
    if p[1] >= 18:
        print(f"{p[0]} é maior de idade.")
        totMaior += 1
    else:
        print(f"{p[0]} é menor de idade.")
        totMenor += 1

print(f"Temos {totMaior} maiores e {totMenor} menores de idade.")