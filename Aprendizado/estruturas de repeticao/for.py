# for loop =    a statement that will execute a block of code 
#               a limited amount of times
#               while loop = unlimited amount of times
#               for loop = limited amount of times


# conta de 50 a 100
#for i in range(50, 100): 
    #print(i)
#print("Fim!")


# conta os segundos de 10 a 1 
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passos = int(input("Passos: "))

for i in range(inicio, fim+1, passos):
    print(i)
print("Fim!")