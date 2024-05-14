# essa função aplica outra função a uma estrutura de dados
# a função map retorna um iterator

def potencia(x):
    return x ** 2

numeros = [1, 2, 3, 4, 5]

# aplicando a função a cada elemento da lista dos numeros
numeros_quadrado = list(map(potencia, numeros))

print(numeros_quadrado)