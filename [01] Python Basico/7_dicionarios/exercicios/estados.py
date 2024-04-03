estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input("Sigla do Estado: "))
    
    # cópia dos estados em brasil
    brasil.append(estado.copy())

for estado in brasil:
    for key, value in estado.items():
        print(f"O campo {key} tem valor {value}")
