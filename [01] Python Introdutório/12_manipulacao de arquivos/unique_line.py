"""
# Abrindo dataset em uma única linha 
f = open('salarios.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows)

# Abrindo dataset em colunas
f = open('salarios.csv', 'r')
data = f.read()
rows = data.split('\n')

full_data = []
for row in rows:
    split_now = row.split(",")
    full_data.append(split_now)
    
# contar linhas do arquivo
count = 0 
for row in full_data:
    count+= 1

print(count)
"""

# Contar colunas em um arquivo
f = open('salarios.csv', 'r')
data = f.read()
rows = data.split('\n')

full_data = []
for row in rows:
    split_now = row.split(",")
    full_data.append(split_now)
    first_row = full_data[0]
    
count = 0
for column in first_row:
    count = count + 1
    
print(count)