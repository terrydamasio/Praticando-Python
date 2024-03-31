# dicionários são estruturas de dados semelhantes a listas, porém conseguimos usar índices literais

dados = dict()
dados = {
    'nome': 'Terry', 
    'idade': 20,
    'peso': 78,
    'altura': 1.80
    }

# adicionar elementos
dados['sexo'] = 'M'

# eliminar elementos
del dados['idade']

# valores
print(dados.values())

# chaves
print(dados.keys())

# itens
print(dados.items())

# percorrendo dicionário
for key, value in dados.items():
    print(f"O {key} é {value}.")