# abrir arquivo para leitura 
arq = open("arquivos/arquivo1.txt", "r")

# ler arquivo
print(arq.read())
print(arq.read())

# contar caracteres
print(arq.tell())

# print(arq.seek(0,0))