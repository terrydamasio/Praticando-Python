from random import randint
from time import sleep
from operator import itemgetter

# 4 jogadores jogam um dado com resultados aleatórios
resultados = {
    'jogador 1': randint(1, 6),
    'jogador 2': randint(1, 6),
    'jogador 3': randint(1, 6),
    'jogador 4': randint(1, 6),
}

ranking = list()
 
print("Valores sorteados: ")
for key, value in resultados.items():
    print(f"O jogador {key} tirou {value}")
    sleep(1)

# ordenando resultados
ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)

print("Ranking de vencedores: ")
for indice, value in enumerate(ranking):
    print(f"{indice+1}º lugar: {value[0]} com {value[1]}.")

# colocar o dicionário em ordem 
# o vencedor tirou o maior número do dado