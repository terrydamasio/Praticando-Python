# o método close é executado automaticamente com o WITH
with open('arquivo_1.py', 'r') as arquivo:
    conteudo = arquivo.read()
print(conteudo)