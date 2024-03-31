from random import randint

numero_sorteado = randint(0, 10)
acertou = False
palpites = 0

print("-- Jogo da Adivinhação --")

while not acertou and palpites < 5:
    numero_escolhido = int(input("Digite um número entre 0 e 10: "))
    palpites += 1

    if numero_escolhido == numero_sorteado:
        acertou = True
        print(f"Parabéns, você acertou com {palpites} tentativas!")
    else: 
        if numero_sorteado > numero_escolhido:
            print(f"Mais... Tentativa {palpites} de 5.")
        elif numero_sorteado < numero_escolhido:
            print(f"Menos... Tentativa {palpites} de 5.")  

print(f"Suas chances acabaram - {palpites}/5. Mas não desista, tente novamente!")
