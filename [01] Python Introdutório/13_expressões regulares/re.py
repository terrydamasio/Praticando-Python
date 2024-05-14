# expressões regulares são padrões usados para combinar ou encontrar ocorrências
import re 

texto = "Meu email é terry@gmail.com e você pode me contatar em terrydamasio@gmail.com"
resultado = len(re.findall("@", texto))
print(resultado)