try: # tente
    a = int(input("Digite um número: "))
except (ValueError, TypeError): # excessão
    print(f"Tivemos um problema com os tipos de dados.")
except Exception as error:
    print(f"Error: {error.__class__}")
else: # se não
    print(f"O resultado é {a}")
finally: # esse comando de bloco sempre é executado
    print("Volte sempre!")