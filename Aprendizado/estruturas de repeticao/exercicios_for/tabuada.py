num = int(input("Digite qual o número você quer exibir a tabuada: "))

print("Tabuada: ")
for i in range(1, 10+1):
    print(f"{num} x {i} = {i * num}")