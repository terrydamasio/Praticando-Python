# list methods/functions
frutas = ["Maçã", "Banana", "Melancia"]
x, y, z = frutas

print(frutas[0])

# lists functions
frutas.append("Uva") # adcionar um elemento
frutas.insert(0, "Uva") # adcionar um elemento na posição x
frutas.sort() # colocar os valores em ordem
frutas.sort(reverse=True) # colocar os valores em ordem inversa
frutas.clear() #limpar uma lista
len(frutas) # saber o tamanho do array

frutas.remove("Banana") # remover um elemento pelo valor  
frutas.pop(3) # remover elemento pelo índice
del frutas[2] # remover elemento pelo índice
frutas.pop() # remove o último elemento 


# condicional para remover 
if frutas['Maçã'] in frutas:
    frutas.remove("Maçã")

# criar listas com range
valores = list(range(0, 10))
print(valores)