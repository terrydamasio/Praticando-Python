# criar uma ficha com doi parametros opcionais: nome e gols
# programa deve mostrar a ficha do jogador, mesmo que não tenha dados informados corretamente

name = str(input("Nome do Jogador: "))
goals = int(input("Número de Gols: "))

def fichaJogador(name = '', goals = 0):
    if name in '':
        name = "<desconhecido>"

    return f"O jogador {name} fez {goals} gol(s) no campeonato."


ficha = fichaJogador(name, goals)
print(ficha)