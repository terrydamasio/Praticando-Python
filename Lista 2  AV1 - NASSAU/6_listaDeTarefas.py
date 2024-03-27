import tkinter as tk
import json

# Função para adicionar uma tarefa
def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa:
        lista_tarefas.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)
        salvar_tarefas()

# Função para listar tarefas
def listar_tarefas():
    try:
        with open("tarefas.json", "r") as arquivo:
            tarefas = json.load(arquivo)
            for tarefa in tarefas:
                lista_tarefas.insert(tk.END, tarefa)
    except FileNotFoundError:
        pass

# Função para marcar como concluída uma tarefa
def marcar_concluida():
    selecao = lista_tarefas.curselection()
    if selecao:
        index = selecao[0]
        lista_tarefas.itemconfig(index, {'bg': 'light green'})
        salvar_tarefas()

# Função para remover tarefa
def remover_tarefa():
    selecao = lista_tarefas.curselection()
    if selecao:
        lista_tarefas.delete(selecao[0])
        salvar_tarefas()

# Função para salvar tarefas em um arquivo JSON
def salvar_tarefas():
    tarefas = lista_tarefas.get(0, tk.END)
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo)

# Configuração da janela
janela = tk.Tk()
janela.title("Aplicativo de Gerenciamento de Tarefas")

# Entrada de tarefa
entrada_tarefa = tk.Entry(janela)
entrada_tarefa.pack(pady=10)
entrada_tarefa.bind("<Return>", lambda event=None: adicionar_tarefa())

# Lista de tarefas
lista_tarefas = tk.Listbox(janela, bg="light yellow")
lista_tarefas.pack()

# Botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

botao_adicionar = tk.Button(frame_botoes, text="Adicionar", command=adicionar_tarefa)
botao_listar = tk.Button(frame_botoes, text="Listar Tarefas", command=listar_tarefas)
botao_marcar_concluida = tk.Button(frame_botoes, text="Marcar como Concluída", command=marcar_concluida)
botao_remover = tk.Button(frame_botoes, text="Remover Tarefa", command=remover_tarefa)

botao_adicionar.grid(row=0, column=0)
botao_listar.grid(row=0, column=1)
botao_marcar_concluida.grid(row=0, column=2)
botao_remover.grid(row=0, column=3)

# Inicializar o aplicativo
listar_tarefas()
janela.mainloop()