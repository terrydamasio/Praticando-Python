import moeda

value = float(input("Digite o preço: R$"))
print(f"A metade do preço de {value} é {moeda.half(value)}")
print(f"O dobro do preço de {value} é {moeda.double(value)}")
print(f"Aumentando 10% de {value}, temos {moeda.incrPercent(value)}")
print(f"Reduzindo 15% de {value}, temos {moeda.decrPercent(value)}")