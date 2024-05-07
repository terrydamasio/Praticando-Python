email = str(input("Digite seu email:"))

posicao = email.find("@")
servidor = email[posicao:]
mail = email[:posicao]

print("Servidor:" + servidor)
print("Nome" + mail)
()