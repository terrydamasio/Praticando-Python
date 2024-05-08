# lists are used to store multiple items in a single variable
# multiple lists 

# 2d lists is a list of lists

marca = ["Volgswagen", "Toyota", "Chevrollet"]
modelo = ["Golf", "Supra", "Hilux"]

carros = [marca, modelo] # junta os arrays marca e modelo
marca = modelo[:] # cria uma cópia de modelo dentro da marca

print(marca)
print(carros)
print(carros[1][0:2]) # modelos golf e supra 
