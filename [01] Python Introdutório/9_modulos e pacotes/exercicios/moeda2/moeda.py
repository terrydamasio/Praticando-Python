# calcula metade
def half(value = 0, format = False):
    res = value / 2
    return res if format is False else formate(res)

# calcula dobro
def double(value = 0, format = False):
    res = value * 2
    return res if format is False else formate(res)

# calcula acrescimo percentual
def incrPercent(value = 0, taxain = 0, format = False):
    res = (value * taxain/100) + value
    return res if format is False else formate(res)

# calcula decrescimo percentual
def decrPercent(value = 0, taxade = 0, format = False):
    res = value - (value * taxade/100)
    return res if format is False else formate(res)


# formata valor -> R$
def formate(value = 0, moeda = 'R$'):
    return f"{moeda}{value:.2f}".replace('.',',')


# resumo das operações
def resumo(value = 0, taxain = 10, taxade = 15):
    print('-'*30) 
    print("Resumo do Valor".center(30)) 
    print('-'*30) 
    
    print(f"Preço analisado {formate(value)}")
    print(f"Metade do preço {half(value, True)}")
    print(f"Dobro do preço {double(value, True)}")
    print(f"Aumento de {taxain}% do preço {incrPercent(value, taxain, True)}")
    print(f"Decrescimo {taxade}% do preço {decrPercent(value, taxade, True)}")
    print('-'*30) 
