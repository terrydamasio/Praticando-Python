from random import randint

# criar tupla
num = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))

# percorrer tupla
for n in num:
    print(f"{n} ")

print(f"O maior valor sorteado foi {max(num)}.")
print(f"O menor valor sorteado foi {min(num)}.")