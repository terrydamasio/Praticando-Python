# criar novo arquivo se não existir -> x = create
arq = open("arquivo_1.txt", "x")

# abrir arquivo para escrever -> w = write
arq = open("arquivo_1.txt", "w") 

# escrevendo no arquivo
arq.write("Aprendendo manipulação de arquivos")
arq.close()

# acrescentando conteúdo -> a = append
arq = open("arquivo_1.txt", "a")
arq.write(" com o curso do datascience academy")
arq.close()

# abrir para ler arquivo -> r = read
arq = open("arquivo_1.txt", "r")
print(arq.read())

# retorna o cursor para início do arquivo
print(arq.seek(0,0))

# ler 10 caracteres do arquivo
print(arq.read(10))

# contar caracteres do arquivo
print(arq.tell())

# deletando arquivo
import os 

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")