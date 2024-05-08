# [expressão for item in interable if condição == True]

# list comprehension
lista_1 = [x for x in range(10)]
print(lista_1)

# imprime x para cada valor de x num range de 10 se x <= 5 
lista_2 = [x for x in range(10) if x <= 5]
print(lista_2)

lista_frutas = ['banana', 'melancia', 'morango', 'uva']
nova_lista = [x for x in lista_frutas if "m" in x]
print(nova_lista)

# dict comprehension
dict_alunos = {'Bob': 68, 'Michel': 84, 'Zico': 57}
dict_alunos_status = {k:v for (k, v) in dict_alunos.items()}
dict_alunos_status = {k: ('Aprovado' if v > 70 else 'Reprovado') for (k, v) in dict_alunos.items()}
print(dict_alunos_status)