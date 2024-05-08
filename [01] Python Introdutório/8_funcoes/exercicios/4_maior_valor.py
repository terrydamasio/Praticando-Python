from time import sleep

# analisar e dizer qual deles é o maior
def bigNum(*num):   
    cont = maior = 0
    print("Analisando os valores passados...")
    for valor in num:
        print(f"{valor} ", end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f"Foram informados {cont} valores ao todo.")
    print(f"O maior valor informado foi {valor}.")

bigNum(1, 2, 3, 4, 5, 6)