# filtra os elementos de uma estrutura de dados
def verificaPar(num):
    if num % 2 ==0:
        return True
    else:
        return False

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]    

filtrarPar = list(filter(verificaPar, lista))
print(filtrarPar)
