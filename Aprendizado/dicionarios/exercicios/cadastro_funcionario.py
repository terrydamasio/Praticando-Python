from datetime import datetime

# criar dicionário
cadastro = dict()

# ler dados (nome, ano nasc, carteira de trab)
print("Cadastro de Funcionários")
print('-'*30)
cadastro['nome'] = str(input("Nome: "))
nasc = int(input("Ano de Nascimento: "))

cadastro['idade'] = datetime.now().year - nasc
cadastro['ctps'] = int(input("Carteira de Trabalho: (0 = não tem) "))
carteira_trab = cadastro['ctps']

if carteira_trab != 0:
    cadastro['contratacao'] = int(input("Ano de contratação: "))
    cadastro['salario'] = float(input("Salário: R$"))
    cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['contratacao'] + 20) - datetime.now().year)

print('-='*30)
print("Funcionário cadastrado com sucesso!")
print('-='*30)

for key, value in cadastro.items():
    print(f"{key.capitalize()}: {value}")