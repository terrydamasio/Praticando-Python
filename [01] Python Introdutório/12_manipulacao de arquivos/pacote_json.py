# Importando o módulo JSON
import json

alunos = {
    'nome': 'Terry Damasio',
    'email': 'terrydamasio@gmail.com',
    'telefone': '81989189090',
}

# convertend dicionário para um objeto json
json.dumps(alunos)

# criando arquivo json
with open('arquivos/alunos.json', 'w') as arquivo:
    arquivo.write(json.dumps(alunos))

# lendo arquivo json
with open('arquivos/alunos.json', 'r') as arquivo:
    alunos = arquivo.read()
    dados = json.loads(alunos)

print(f"{dados['nome']} - {dados['email']} - {dados['telefone']}")