# tuplas = são usadas para armazenar vários valores 
# em uma única variável que não pode ser mudada
# obs: tuplas são constantes, ou seja, não consegue mudar durante a execução do código

carros = ("Golf", "Jetta", "Virtus", "Gol", "Jetta")

#print(carros[2])
#print(carros[0:2])

# percorrendo uma tupla
for carro in carros:
    print(carro)

for cont in range(0, len(carros)):
    print(f"Esses são os carros que eu tenho: {carros[cont]} na posição {cont}")

for pos, carro in enumerate(carros):
    print(f"Esses são os carros que eu tenho: {carro} na posição {pos}")
