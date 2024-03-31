# criar dicionário
jogador = {
    'nome': str(input('Nome do Jogador: ')),
    'gols': []
}

# ler partidas jogou
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

# ler quantidade de gols feito por partida
for c in range(1, partidas+1):
    jogador['gols'].append(int(input(f"Quantos gols na partida {c}? ")))
    
# total de gols
jogador['total'] = sum(jogador['gols'])

print('-='*30)
print('Tabela:')

# percorrer valores
for key, value in jogador.items():
    print(f"{key.capitalize()}: {value}")

print('-='*30)
print(f"O jogador {jogador['nome']} jogou {partidas} partidas.")

# formatando resposta
for key, value in enumerate(jogador['gols']):
    print(f"=> Na partida {key+1}, {jogador['nome']} fez {value} gols.")

