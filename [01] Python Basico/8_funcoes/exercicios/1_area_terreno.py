# receber dimensões de um terreno e calcular a área

print("Controle de Terrenos")
print("-"*30)
largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))

def calcArea(l, c):
    area = l * c
    return f"A área do seu terreno {l} x {c} é de {area}m2"

print(calcArea(largura, comprimento))

