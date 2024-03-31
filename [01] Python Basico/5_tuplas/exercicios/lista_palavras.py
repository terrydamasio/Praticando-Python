# criar lista de palavras
palavras = ('aprender', 'estudar', 'programar', 'cavalgar', 
            'ler', 'trabalhar', 'correr', 'ajudar', 'pular')

# separar as palavras
for palavra in palavras:
    print(f"\nNa palavra '{palavra.upper()}' temos ", end='')

    # separar vogais
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
