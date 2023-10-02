notas = ['a', 'b', 'c', 'd']

a = float(input("Digite a primeira nota: "))
b = float(input("Digite a segunda nota: "))
c = float(input("Digite a terceira nota: "))
d = float(input("Digite a quarta nota: ")) 

media = (a + b + c + d)/4

if (media >= 9):
    print("\nSua media foi: A+ ", media, ".\nParabéns, você foi aprovado!")
elif (media >= 7 and media <= 8.9):
    print("\nSua media foi: B ", media, ".\nParabéns, você foi aprovado!")
elif (media >= 5 and media <= 6.9):
    print("\nSua media foi: C ", media, ".\nEstude mais, você foi reprovado!")
elif (media >= 3 and media <= 4.9):
    print("\nSua media foi: D ", media, ".\nEstude mais, você foi reprovado!")
elif (media >= 0 and media <= 2.9):
    print("\nSua media foi: F ", media, ".\nEstude mais, você foi reprovado!")   

