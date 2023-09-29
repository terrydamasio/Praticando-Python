#Comentário de uma linha
"""
Comentário de várias linhas
"""

print("Olá UNINASSAU") #Exibir na tela


#VARIÁVEIS

#criando variável
x = 1

#especificar tipo de dado
x = str(3)
y = int(3)
z = float(3)

#obter tipo de dados
print(type(x))

#valores para várias variáveis
x, y, z = 1, 2, 3

#descompactação: Caso você tenha uma array, você consegue descompactar esse array em variáveis
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)