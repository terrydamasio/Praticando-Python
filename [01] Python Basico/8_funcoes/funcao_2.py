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
# escopo de variáveis
# retorno