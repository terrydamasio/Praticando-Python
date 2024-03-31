aluno = dict()

# ler nome e média
aluno['nome'] = str(input("Nome do Aluno: "))
aluno['media'] = float(input("Média do Aluno: "))

# calcular situação (aprovado ou reprovado)
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif  3 < aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

# mostrar o conteúdo na tela
print(f"Nome: {aluno['nome']}")
print(f"Média de {aluno['nome']}: {aluno['media']}")
print(f"Situação de {aluno['nome']}: {aluno['situacao']}")