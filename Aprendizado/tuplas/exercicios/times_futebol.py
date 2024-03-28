# listar tabela do campeonato brasileiro na ordem
times = ('Athletico-PR', 'Athletico-GO', 'Bahia', 'Botafogo', 
        'Bragantino', 'Corinthians', 'Flamengo', 'Fluminense', 
        'Palmeiras', 'Internacional', 'São Paulo', 'Vasco')

# mostrar os 5 primeiros
print(f"Os 5 primeiros times são: {times[:5]}")
print("-"*30)

# mostrar os 4 ultimos
print(f"Os 4 últimos times são: {times[-4:]}")
print("-"*30)

# listar times em ordem alfabética
print(f"Times em ordem alfabética: {sorted(times)}")
print("-"*30)

# posição do time chapecoense
print(f"O Flamengo está na {times.index('Flamengo') + 1}º posição ")