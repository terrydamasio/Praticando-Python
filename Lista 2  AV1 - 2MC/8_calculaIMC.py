# Função para calcular o IMC
def calcular_imc(peso, altura):
    try:
        altura_metros = altura / 100  # Converter altura para metros
        imc = peso / (altura_metros ** 2)
        return imc
    except ZeroDivisionError:
        return None

# Função para interpretar o IMC
def interpretar_imc(imc):
    if imc is None:
        return "Por favor, insira um valor válido para a altura."
    elif imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade Grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade Grau 2"
    else:
        return "Obesidade Grau 3"

# Solicitar ao usuário o peso e a altura
peso = float(input("Insira o seu peso (em kg): "))
altura = float(input("Insira a sua altura (em cm): "))

# Calcular o IMC
imc = calcular_imc(peso, altura)

# Interpretar o resultado do IMC
resultado_imc = interpretar_imc(imc)

# Exibir o resultado
if imc is not None:
    print(f"Seu IMC é: {imc:.2f}")
    print(f"Classificação: {resultado_imc}")
else:
    print("Altura inválida. Por favor, insira um valor válido para a altura.")