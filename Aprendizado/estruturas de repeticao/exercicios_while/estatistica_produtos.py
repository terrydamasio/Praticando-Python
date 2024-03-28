total = totMil = menor = cont = 0
barato = ' '
while True:
    produto = str(input("Nome do produto: "))
    preco = float(input("Preço: R$"))
    cont += 1
    total += preco

    if preco > 1000:
        totMil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else: 
        if preco < menor: 
            menor = preco
            barato = produto
        
    resp = ' '
    while resp not in 'SN': 
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == 'N':
        break
print('-------Fim do programa-------')
print(f'O total da compra foi {total:10.2f}')
print(f'Temos {totMil} custando mais de R$1.000,00')
print(f'O produto mais barato foi {barato} e custa {menor:.2f}.')