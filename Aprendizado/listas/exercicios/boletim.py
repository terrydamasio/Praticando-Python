ficha = list()

while True:
    nome = str(input("Nome: "))
    nota_1 = float(input("Nota 1: "))
    nota_2 = float(input("Nota 2: "))

    media = (nota_1 + nota_2) / 2
    ficha.append([nome, [nota_1, nota_2], media])
    
    opcao = str(input("Deseja continuar? [S/N]")).strip().upper()

    if opcao in "N":
        break

print("="*30)
print(f"{'Nº':<4}{'Nome':<10}{'Média':<8}")
print("-"*26)

for indice, aluno in enumerate(ficha):
    print(f"{indice:<4}{aluno[0]:<10}{aluno[2]:<8.1f}")

while True:
    opcao = int(input("Você quer ver as notas de qual aluno? [999 = Sair]"))

    if opcao in 999:
        print("Saindo...")
        break
    if opcao <= len(ficha) - 1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}.')