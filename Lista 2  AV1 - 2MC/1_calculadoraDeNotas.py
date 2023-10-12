# Função para calcular a nota correspondente com base na média
def calcular_nota(media):
    if media >= 9:
        return 'A'
    elif media >= 8:
        return 'B'
    elif media >= 7:
        return 'C'
    elif media >= 6:
        return 'D'
    else:
        return 'F'

# Solicita ao usuário o número de notas
num_notas = int(input("Quantas notas você deseja inserir? "))

# Inicializa a variável que armazenará a soma das notas
soma_notas = 0

# Solicita e calcula as notas
for i in range(num_notas):
    nota = float(input(f"Insira a nota {i + 1}: "))
    soma_notas += nota

# Calcula a média
media = soma_notas / num_notas

# Chama a função para obter a nota correspondente
nota_correspondente = calcular_nota(media)

# Exibe a média e a nota correspondente
print(f'A média das notas é {media:.2f} e a nota correspondente é {nota_correspondente}')