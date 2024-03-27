# nested loops = the "inner loop" will finish all of it's interations before 
#                finishing one interaction 

rows = int(input("Digite a quantidade de linhas: "))
columns = int(input("Digite quantas colunas: "))
symbol = input("Digite um símbolo: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="") 
    print()