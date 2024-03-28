listagem = ('Caneta', 2, 
            'Lapis', 1.50,
            'Borracha', 3,
            'Caderno', 30,
            'Estojo', 25,
            'Mochila', 124.90)
print('-'*30)
print('Lista de Preços')
print('-'*30)


for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end='')
    elif pos % 2 == 1:
        print(f"R${listagem[pos]:>7.2f}")