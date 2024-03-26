import random

aluno_1 = str(input("Digite o aluno 1: "))
aluno_2 = str(input("Digite o aluno 2: "))
aluno_3 = str(input("Digite o aluno 3: "))
aluno_4 = str(input("Digite o aluno 4: "))

alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
sorteado = random.choice(alunos)
apresentacao = random.shuffle(alunos)

print(f"O aluno sorteado foi: {sorteado}")
print(f"A ordem de apresentação é: {apresentacao}")
