matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = maior = soma_coluna = 0

# adicionar valores na matriz
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"Digite um valor para a posição [{linha}, {coluna}]: "))

print('='*30)

# formatar valores
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]}]", end='')

        #soma pares
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
    print()

print('='*30)
print(f'A soma dos valores pares é {soma_pares}.')

# soma coluna 3
for linha in range (0, 3):
    soma_coluna += matriz[linha][2]
print(f"A soma dos valores da terceira coluna é {soma_coluna}.")

# maior valor da segunda linha
for coluna in range (0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f"O maior valor da segunda linha é {maior}.")