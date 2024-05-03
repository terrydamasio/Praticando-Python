import sched
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Função para enviar e-mail
def enviar_email(remetente, senha, destinatario, assunto, mensagem):
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto
    msg.attach(MIMEText(mensagem, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(remetente, senha)
    text = msg.as_string()
    server.sendmail(remetente, destinatario, text)
    server.quit()

# Função para enviar notificação por e-mail
def enviar_notificacao_email(remetente, senha, destinatario, mensagem):
    enviar_email(remetente, senha, destinatario, "Notificação do Condomínio", mensagem)

# Função para enviar notificação por SMS
def enviar_notificacao_sms(numero, mensagem):
    print(f"Enviando SMS para {numero}: {mensagem}")

# Função para enviar notificação por WhatsApp
def enviar_notificacao_whatsapp(numero, mensagem):
    print(f"Enviando mensagem pelo WhatsApp para {numero}: {mensagem}")

# Cadastro de condôminos
def cadastrar_condominos():
    condominos = {}
    with open('condominos.txt', 'r') as file:
        for line in file:
            nome, email, telefone = line.strip().split(',')
            condominos[nome] = {'email': email, 'telefone': telefone}
    while True:
        nome = input("Digite o nome do condômino (ou deixe em branco para encerrar): ")
        if not nome:
            break
        email = input("Digite o e-mail do condômino: ")
        telefone = input("Digite o telefone do condômino: ")
        condominos[nome] = {'email': email, 'telefone': telefone}
    with open('condominos.txt', 'w') as file:
        for nome, info in condominos.items():
            file.write(f"{nome},{info['email']},{info['telefone']}\n")

# Cadastro de áreas comuns
def cadastrar_areas_comuns():
    areas_comuns = []
    with open('areas_comuns.txt', 'r') as file:
        for line in file:
            areas_comuns.append(line.strip())
    while True:
        area = input("Digite o nome de uma área comum (ou deixe em branco para encerrar): ")
        if not area:
            break
        areas_comuns.append(area)
    with open('areas_comuns.txt', 'w') as file:
        for area in areas_comuns:
            file.write(f"{area}\n")
    return areas_comuns

# Reserva de área comum
def reservar_area_comum(areas_comuns):
    print("Áreas comuns disponíveis:", areas_comuns)
    condomino = input("Digite o nome do condômino que deseja fazer a reserva: ")
    area_comum = input("Digite o nome da área comum que deseja reservar: ")
    data = input("Digite a data da reserva: ")
    with open('reservas.txt', 'a') as file:
        file.write(f"{condomino},{area_comum},{data}\n")

# Envio de notificações
def enviar_notificacoes():
    tipo_notificacao = input("Digite o tipo de notificação que deseja enviar (e-mail/sms/whatsapp): ")
    mensagem = input("Digite a mensagem da notificação: ")
    if tipo_notificacao == "e-mail":
        remetente = input("Digite o seu e-mail: ")
        senha = input("Digite a sua senha: ")
        destinatario = input("Digite o e-mail do destinatário: ")
        enviar_notificacao_email(remetente, senha, destinatario, mensagem)
    elif tipo_notificacao == "sms":
        numero = input("Digite o número de telefone do destinatário: ")
        enviar_notificacao_sms(numero, mensagem)
    elif tipo_notificacao == "whatsapp":
        numero = input("Digite o número de telefone do destinatário (com código do país, sem espaços ou caracteres especiais): ")
        enviar_notificacao_whatsapp(numero, mensagem)
    else:
        print("Tipo de notificação inválido.")

# Menu principal
def menu():
    print("\n===== MENU =====")
    print("1. Cadastrar Condôminos")
    print("2. Cadastrar Áreas Comuns")
    print("3. Reservar Área Comum")
    print("4. Enviar Notificações")
    print("0. Sair")

# Função principal
def main():
    areas_comuns = []
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_condominos()
        elif opcao == "2":
            areas_comuns = cadastrar_areas_comuns()
        elif opcao == "3":
            reservar_area_comum(areas_comuns)
        elif opcao == "4":
            enviar_notificacoes()
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
