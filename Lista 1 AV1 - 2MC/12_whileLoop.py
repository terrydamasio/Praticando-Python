# while loop =  a statement that will execute a block of code, as long
#               the condition remains true

name = input("Digite o seu nome: ")

while len(name) == 0 or len(name) < 4:
    name = input("Digite o seu nome: ")

print("Seja bem vindo, " + name)
