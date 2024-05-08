# interactive help -> python -> help(func) 
print(input.__doc__)
help(input)

# docstrings -> string de documentação 
def cont(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f"{c}", end='')
        c += p

# argumentos opcionais
def sum(a, b, c = 0):
    s = a + b + c
    print(f"A soma vale {s}")
#sum(8, 4)

# escopo de variáveis => local onde a variável vai existir ou não
# retorno => return 