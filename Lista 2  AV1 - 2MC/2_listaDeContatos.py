import csv
import os

# Função para adicionar um novo contato
def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    
    with open('agenda.csv', 'a', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow([nome, telefone])
    print(f"Contato {nome} adicionado com sucesso!")

# Função para listar todos os contatos
def listar_contatos():
    with open('agenda.csv', 'r') as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        for linha in reader:
            print(f"Nome: {linha[0]}, Telefone: {linha[1]}")

# Função para buscar um contato
def buscar_contato():
    nome_busca = input("Digite o nome que deseja buscar: ")
    
    with open('agenda.csv', 'r') as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        encontrado = False
        for linha in reader:
            if nome_busca.lower() in linha[0].lower():
                print(f"Nome: {linha[0]}, Telefone: {linha[1]}")
                encontrado = True
        if not encontrado:
            print("Contato não encontrado.")

# Função para remover um contato
def remover_contato():
    nome_remover = input("Digite o nome do contato que deseja remover: ")
    
    with open('agenda.csv', 'r') as arquivo_csv:
        linhas = list(csv.reader(arquivo_csv))
    
    encontrado = False
    with open('agenda.csv', 'w', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        for linha in linhas:
            if nome_remover.lower() == linha[0].lower():
                print(f"Contato {linha[0]} removido com sucesso!")
                encontrado = True
            else:
                writer.writerow(linha)
    
    if not encontrado:
        print("Contato não encontrado.")

# Verifica se o arquivo CSV da agenda existe e cria se não existir
if not os.path.isfile('agenda.csv'):
    with open('agenda.csv', 'w', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow(["Nome", "Telefone"])

# Loop principal do programa
while True:
    print("\nEscolha uma opção:")
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Buscar contato")
    print("4 - Remover contato")
    print("5 - Sair")
    
    opcao = input("Opção: ")
    
    if opcao == '1':
        adicionar_contato()
    elif opcao == '2':
        listar_contatos()
    elif opcao == '3':
        buscar_contato()
    elif opcao == '4':
        remover_contato()
    elif opcao == '5':
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")