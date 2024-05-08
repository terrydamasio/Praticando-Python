import datetime

# funcao voto com ano de nasc
nasc = int(input("Digite sua data de nascimento: "))

def votar(nasc):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - nasc

    if idade < 16:
        return f"Com {idade} anos: Voto Negado!"
    elif 16 <= idade < 18:
        return f"Com {idade} anos: Voto Opcional!"
    elif idade > 18:
        return f"Com {idade} anos: Voto Obrigatório!"

result = votar(nasc)
print(result)