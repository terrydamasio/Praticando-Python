import csv
import os

# Nome do arquivo CSV
FILENAME = 'usuarios.csv'

# Função para inicializar o arquivo CSV com cabeçalhos, se não existir
def inicializar_csv():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Nome', 'Email'])

# Função para obter o próximo ID
def obter_proximo_id():
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.DictReader(file)
            ids = [int(row['ID']) for row in reader]
            return max(ids) + 1 if ids else 1
    except FileNotFoundError:
        return 1

# Função para criar um novo usuário
def criar_usuario(nome, email):
    novo_id = obter_proximo_id()
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([novo_id, nome, email])
    print(f'Usuário {nome} adicionado com sucesso!')

# Função para ler todos os usuários
def ler_usuarios():
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print('Nenhum usuário encontrado. O arquivo CSV ainda não foi criado.')

# Função para atualizar um usuário pelo ID
def atualizar_usuario(id, novo_nome, novo_email):
    atualizado = False
    usuarios = []
    
    with open(FILENAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row['ID']) == id:
                row['Nome'] = novo_nome
                row['Email'] = novo_email
                atualizado = True
            usuarios.append(row)
    
    if atualizado:
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['ID', 'Nome', 'Email'])
            writer.writeheader()
            writer.writerows(usuarios)
        print(f'Usuário com ID {id} atualizado com sucesso!')
    else:
        print(f'Usuário com ID {id} não encontrado.')

# Função para deletar um usuário pelo ID
def deletar_usuario(id):
    deletado = False
    usuarios = []
    
    with open(FILENAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row['ID']) != id:
                usuarios.append(row)
            else:
                deletado = True
    
    if deletado:
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['ID', 'Nome', 'Email'])
            writer.writeheader()
            writer.writerows(usuarios)
        print(f'Usuário com ID {id} deletado com sucesso!')
    else:
        print(f'Usuário com ID {id} não encontrado.')

# Inicializando o arquivo CSV
inicializar_csv()

# Exemplo de uso das funções
criar_usuario('João Silva', 'joao@example.com')
criar_usuario('Maria Souza', 'maria@example.com')
ler_usuarios()
atualizar_usuario(1, 'João da Silva', 'joao.silva@example.com')
ler_usuarios()