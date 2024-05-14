# importando a biblioteca
from platform import python_version
from functools import reduce

lista = [47, 11, 42, 13]

def soma(x, y):
    soma = x + y
    return soma

# faz a redução de um conjunto de dados em um único resultado
result = reduce(soma, lista)
print(result)