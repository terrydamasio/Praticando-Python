# funções são como uma rotina, ou seja, sao tarefas que você executa repetidas vezes e você armazena em uma função para evitar redundancia de código 

nome = str(input("Digite seu nome: "))

def showName(name):
    return name

print(showName(nome))

# empacotar parâmetros -> Permite receber vários parâmetros sem saber previamente quantos parâmetros serão criados
def showNumbers(*num):
    return num

print(showNumbers(1, 2, 3, 4, 5))