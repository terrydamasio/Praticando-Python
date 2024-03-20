from datetime import datetime, timedelta

hora_entrada = input("Digite a hora de entrada (13h20): ")
hora_saida = input("Digite a hora de saída (16h20): ")

# 1h = 60 min = 3600 seg
min_entrada = int(hora_entrada[-2:])
hora_entrada = int(hora_entrada[0:2])

min_saida = int(hora_saida[-2:])
hora_saida = int(hora_saida[0:2])

#                   hr  min  seg
hora_entrada = timedelta(hours=hora_entrada, minutes=min_entrada)
hora_saida = timedelta(hours=hora_saida, minutes=min_saida)
#hora_saida = hora_saida.strftime('%H:%M')

temp_estacionamento = hora_saida - hora_entrada

if temp_estacionamento != timedelta(hours=0, minutes=0, seconds=0):

    if temp_estacionamento <= timedelta(hours=1):
        taxa_estacionamento = 5.00
        print(f"O tempo de uso do estacionamento foi de {temp_estacionamento}. Taxa a pagar R$ {taxa_estacionamento}")
    
    elif temp_estacionamento > timedelta(hours=1):
        if temp_estacionamento >= timedelta(hours=1) and temp_estacionamento < timedelta(hours=2):
            taxa_estacionamento = 5 + 3;
            print(f"O tempo de uso do estacionamento foi de {temp_estacionamento}. Taxa a pagar R$ {taxa_estacionamento} ")
        elif temp_estacionamento >= timedelta(hours=2):
            taxa_estacionamento = (temp_estacionamento * 5) + 3;
            print(f"O tempo de uso do estacionamento foi de {temp_estacionamento}. Taxa a pagar R$ {taxa_estacionamento} ")
else:
    print("Taxa a pagar R$ 0,00")