salarioPorHora = float(input("Quanto você ganha por hora? "))
horasTrabalhadas = float(input("Quantas horas você trabalhou nesse mês? "))

if not salarioPorHora <= 0: 
    print("Digite um salário válido") 
else: 
    salarioMes = salarioPorHora * horasTrabalhadas   
    salarioBonus = salarioMes * 1.10

    print("Seu salário bruto nesse mês é: ", salarioMes)
    print("Seu salário nesse mês com o bonûs: ", salarioBonus)
