# while loop =  a statement that will execute a block of code, as long
#               the condition remains true

#name = input("Digite o seu nome: ")

#while len(name) == 0 or len(name) < 4:
#    name = input("Digite o seu nome: ")
#print("Seja bem vindo, " + name)

# INTERROMPENDO REPETIÇÕES 
# break = used to terminate the loop entirely 
# continue = skips to the next interation 
# pass = does nothing

while True: 
    name = input("Digite o seu nome: ")
    if name != "":
        break 