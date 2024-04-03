from random import randint
from time import sleep

def sort(list):
    print("Sorteando valores: ", end='')
    for cont in range(0,5):
        num = (randint(1, 10))
        list.append(num)
        print(f"{num} ", end='', flush='True')
        sleep(0.3)

def sumPar(list):
    summ = 0
    for value in list:
        if value % 2 == 0:
            summ += value
    print("-"*30)
    print(f"\nA soma dos valores pares de {list} é igual a {summ}")


numbers = list()
sort(numbers)
sumPar(numbers)
