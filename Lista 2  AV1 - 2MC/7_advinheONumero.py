import random

# Gere um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

tentativas = 0
max_tentativas = 10

print("Bem-vindo ao jogo de adivinhação! Tente adivinhar o número secreto entre 1 e 100.")

while tentativas < max_tentativas:
    tentativa = int(input("Tentativa {} de {}. Digite um número: ".format(tentativas + 1, max_tentativas)))
    
    if tentativa < numero_secreto:
        print("Tente um número maior.")
    elif tentativa > numero_secreto:
        print("Tente um número menor.")
    else:
        print("Parabéns! Você adivinhou o número secreto ({}) em {} tentativas.".format(numero_secreto, tentativas + 1))
        break
    
    tentativas += 1

if tentativas == max_tentativas:
    print("Fim das tentativas. O número secreto era {}.".format(numero_secreto))
