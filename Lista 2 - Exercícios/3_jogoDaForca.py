import random

# Lista de palavras para o jogo da forca
palavras = ['python', 'java', 'ruby', 'javascript', 'php', 'csharp', 'typescript', 'swift']

# Função para escolher uma palavra aleatória da lista
def escolher_palavra():
    return random.choice(palavras)

# Função para exibir a palavra oculta com letras adivinhadas
def exibir_palavra_oculta(palavra, letras_adivinhadas):
    resultado = ''
    for letra in palavra:
        if letra in letras_adivinhadas:
            resultado += letra
        else:
            resultado += '_'
    return resultado

# Função principal do jogo da forca
def jogo_da_forca():
    palavra_secreta = escolher_palavra()
    letras_adivinhadas = []
    tentativas = 6  # Número máximo de tentativas

    print("Bem-vindo ao Jogo da Forca!")
    
    while tentativas > 0:
        palavra_oculta = exibir_palavra_oculta(palavra_secreta, letras_adivinhadas)
        print(f"Palavra: {palavra_oculta}")
        print(f"Tentativas restantes: {tentativas}")
        
        if palavra_oculta == palavra_secreta:
            print("Parabéns! Você adivinhou a palavra corretamente.")
            break
        
        letra = input("Adivinhe uma letra: ").lower()
        
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, insira uma letra válida.")
            continue
        
        if letra in letras_adivinhadas:
            print("Você já adivinhou essa letra.")
            continue
        
        letras_adivinhadas.append(letra)
        
        if letra not in palavra_secreta:
            tentativas -= 1
            print("Letra incorreta. Tente novamente.")
    
    if tentativas == 0:
        print("Você perdeu! A palavra secreta era: " + palavra_secreta)

# Inicia o jogo da forca
jogo_da_forca()