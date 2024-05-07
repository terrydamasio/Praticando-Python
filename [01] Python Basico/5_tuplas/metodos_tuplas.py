lanche_1 = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') 
lanche_2 = ('Sanduíche', 'Doce')
lanches = lanche_1 + lanche_2

# colocar em ordem
print(sorted(lanche_1))

# contar elementos
print(lanche_1.count("Hamburguer"))

# posição do elemento
print(lanche_1.index("Suco"))

print(lanches)
# deletar elemento
del(lanches)