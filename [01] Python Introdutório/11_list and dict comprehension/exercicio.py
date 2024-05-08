lista_precos = [500, 1000, 2000, 3000]
imposto = [preco * 0.5 for preco in lista_precos if preco > 1000]

print(imposto)