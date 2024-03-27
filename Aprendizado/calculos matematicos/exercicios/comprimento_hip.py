import math

cateto_oposto = float(input("Digite o valor do cateto oposto: "))
cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))

hipotenusa = math.sqrt((cateto_adjacente**2) + (cateto_oposto**2))
print(hipotenusa)