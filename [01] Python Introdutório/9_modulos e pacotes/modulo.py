# modularização se consiste em dividir um grande sistema em pequenos módulos, aumentando a legibilidade e manutenção do código
# importando módulo 
import calc_modulo

num = int(input("Digite um valor: "))
fat = calc_modulo.fatorial(num)
print(f"O fatorial de {num} é  {fat}.")

# bibliotecas => pastas que contém módulos separados por assuntos. Dentro de cada biblioteca, precisa ter um arquivo "__init__.py" 
