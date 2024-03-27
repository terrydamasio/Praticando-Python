# Função para mostrar a lista de filmes e horários
def mostrar_lista_de_filmes():
    print("Escolha um filme e horário:")
    print("1. Filme A - 14:00")
    print("2. Filme B - 16:30")
    print("3. Filme C - 19:00")

# Função para realizar uma reserva
def realizar_reserva(filme, horario, quantidade):
    with open("reservas.txt", "a") as arquivo_reservas:
        arquivo_reservas.write(f"Filme: {filme}, Horário: {horario}, Quantidade: {quantidade}\n")
    print("Reserva realizada com sucesso!")

# Função principal do sistema de reservas
def sistema_de_reservas():
    while True:
        mostrar_lista_de_filmes()
        escolha = input("Escolha o número do filme e horário (ou 'q' para sair): ")

        if escolha.lower() == 'q':
            print("Obrigado por usar o sistema de reservas. Até logo!")
            break

        try:
            escolha = int(escolha)
            if escolha in [1, 2, 3]:
                quantidade = int(input("Quantos ingressos deseja comprar? "))
                if quantidade > 0:
                    filmes = ["Filme A", "Filme B", "Filme C"]
                    horarios = ["14:00", "16:30", "19:00"]
                    filme_escolhido = filmes[escolha - 1]
                    horario_escolhido = horarios[escolha - 1]
                    realizar_reserva(filme_escolhido, horario_escolhido, quantidade)
                else:
                    print("A quantidade deve ser maior que zero.")
            else:
                print("Escolha inválida. Por favor, escolha um número de filme válido.")
        except ValueError:
            print("Escolha inválida. Por favor, insira um número válido.")

# Iniciar o sistema de reservas
sistema_de_reservas()