# lists are used to store multiple items in a single variable
# multiple lists 

frutas = ["Maçã", "Banana", "Melancia"]
x, y, z = frutas

print(frutas[0])

# lists functions
# frutas.append("Uva")
# frutas.remove("Banana")
# frutas.pop()
# frutas.sort()
# frutas.clear()

frutas.insert(0, "Melão")

for x in frutas:
    print(x)