# Dicionário com taxas de câmbio fixas (a partir de dólares)
taxas_de_cambio = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.75,
    "JPY": 110.0,
    "CAD": 1.25,
}

# Função para converter moedas
def converter_moeda(valor, moeda_origem, moeda_destino):
    if moeda_origem not in taxas_de_cambio or moeda_destino not in taxas_de_cambio:
        return "Moeda não suportada."
    
    taxa_origem = taxas_de_cambio[moeda_origem]
    taxa_destino = taxas_de_cambio[moeda_destino]
    
    valor_convertido = valor * (taxa_destino / taxa_origem)
    return valor_convertido

# Função principal do conversor de moedas
def conversor_de_moedas():
    print("Bem-vindo ao Conversor de Moedas!")

    while True:
        print("\nEscolha uma opção:")
        print("1 - Converter moeda")
        print("2 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            moeda_origem = input("Digite a moeda de origem (ex: USD, EUR, GBP): ").upper()
            moeda_destino = input("Digite a moeda de destino (ex: USD, EUR, GBP): ").upper()
            valor = float(input("Digite o valor a ser convertido: "))

            resultado = converter_moeda(valor, moeda_origem, moeda_destino)
            if resultado != "Moeda não suportada.":
                print(f"Valor convertido: {resultado:.2f} {moeda_destino}")
            else:
                print(resultado)
        elif opcao == "2":
            print("Obrigado por usar o Conversor de Moedas. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Inicia o conversor de moedas
conversor_de_moedas()