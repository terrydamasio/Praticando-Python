# CSV (Comma-Separated Values) é um formato de arquivo que armazena dados tabulares.
# Cada linha CSV representa uma linha de uma tabela e as colunas são separadas por ','

import csv
    
# escrever em arquivos csv
with open('clientes.csv', 'w') as arquivo:
    # cria objeto para escrever
    w = csv.writer(arquivo)
    
    # escreve no arquivo linha a linha
    w.writerow(('Nome', 'Email', 'Telefone'))
    w.writerow(('Terry Damasio', 'terrydamasio610@gmail.com', '81989189090'))
    w.writerow(('Kerry Muniz', 'kerrymuniz@gmail.com', '81989189090'))
    w.writerow(('Eduardo Americo', 'eduardoamerico@gmail.com', '81989189090'))
    
# ler arquivos csv
with open('clientes.csv', 'r', encoding='utf8', newline = '\r\n') as arquivo:
    # criar objeto para ler
    r = csv.reader(arquivo)
    
    # loop para leitura linha a linha 
    for x in r:
        print(x)
        
# lista com dados do arquivo
with open('clientes.csv', 'r') as arquivo:
    r = csv.reader(arquivo)
    dados = list(r)
    
print(dados)

# imprimindo linha a linha a partir da segunda
for linha in dados[1:]:
    print(linha)