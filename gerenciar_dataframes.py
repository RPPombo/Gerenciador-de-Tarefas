import pandas as pd
from auxiliares import *
import tkinter as tk
from frame_direita import atualizar_frame_direita 

def salvar_arquivo(janela_principal: tk.Tk):
    # Salva o dataframe no arquivo escolhido
    janela_principal.df.to_csv(janela_principal.caminho_arquivo, sep = ";", index = False)

def adicionar_tarefa(janela_principal: tk.Tk):
    # Criando uma janela de input
    janela = tk.Toplevel(janela_principal)
    janela.title("Input de tarefa")
    centralizar_janela(janela, 400, 200)

    tk.Label(janela, text="Nome da tarefa:").pack(pady=(20, 5))
    entrada_tarefa = tk.Entry(janela, width=25)
    entrada_tarefa.pack(pady=(0, 10))

    def adicionar():
        tarefa = entrada_tarefa.get().strip()

        if tarefa:
            nova_linha = pd.DataFrame({'Tarefa': [tarefa], 'Status': ['Não Iniciada']})
            janela_principal.df = pd.concat([janela_principal.df, nova_linha], ignore_index=True)
            atualizar_frame_direita(janela_principal)
            janela.destroy()
        else:
            tk.Label(janela, text="Digite um nome válido!", fg="red").pack()

    tk.Button(janela, text="Adicionar", command=adicionar).pack(pady=(0, 10))

def atualizar_status(janela_principal: tk.Tk):
    # Criando uma janela de input
    janela = tk.Toplevel(janela_principal)
    janela.title("Input de Status")
    centralizar_janela(janela, 400, 200)

    tk.Label(janela, text="Índice da Tarefa:").pack(pady=(20, 5))
    entrada_indice = tk.Entry(janela, width=25)
    entrada_indice.pack(pady=(0, 10))
    tk.Label(janela, text="Status:").pack(pady=(20,5))
    entrada_status = tk.Entry(janela, width= 25)
    entrada_status.pack(pady=(0,10))

    def atualizar():
        indice = entrada_indice.get().strip()
        status = entrada_status.get().strip()
        
        if status and indice:
            try:
                janela_principal.df.loc[int(indice), "Status"] = status
                atualizar_frame_direita(janela_principal)
                janela.destroy()
            except (IndexError, ValueError):
                tk.Label(janela, text="Index inválido!", fg="red").pack() 
        else:
           tk.Label(janela, text="Preencha corretamente os campos!", fg="red").pack() 

    tk.Button(janela, text="Atualizar", command=atualizar).pack(pady=(0,10))

def atualizar_tarefa(janela_principal: tk.Tk):
    # Criando uma janela de input
    janela = tk.Toplevel(janela_principal)
    janela.title("Input de Tarefa")
    centralizar_janela(janela, 400, 200)

    tk.Label(janela, text="Índice da Tarefa:").pack(pady=(20, 5))
    entrada_indice = tk.Entry(janela, width=25)
    entrada_indice.pack(pady=(0, 10))
    tk.Label(janela, text="Tarefa:").pack(pady=(20,5))
    entrada_tarefa = tk.Entry(janela, width= 25)
    entrada_tarefa.pack(pady=(0,10))

    def atualizar():
        indice = entrada_indice.get().strip()
        tarefa = entrada_tarefa.get().strip()

        if tarefa and indice:
            try:
                janela_principal.df.loc[int(indice), "Tarefa"] = tarefa
                atualizar_frame_direita(janela_principal)
                janela.destroy()
            except (IndexError, ValueError):
                tk.Label(janela, text="Index inválido!", fg="red").pack()
        else:
            tk.Label(janela, text="Preencha corretamente os campos!", fg="red").pack() 

    tk.Button(janela, text="Atualizar", command=atualizar).pack(pady=(0,10))