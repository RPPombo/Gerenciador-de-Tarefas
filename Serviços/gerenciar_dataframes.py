import pandas as pd
from Serviços.auxiliares import *
import tkinter as tk
from Tela.Frames.frame_direita import atualizar_frame_direita
from time import localtime, strftime, sleep

def salvar_arquivo(janela_principal: tk.Tk):
    # Salva o dataframe no arquivo escolhido
    janela_principal.df.to_csv(janela_principal.caminho_arquivo, sep = ";", index = False)
    janela = tk.Toplevel(janela_principal)
    janela.title("Salvamento")
    centralizar_janela(janela, 400, 100)

    tk.Label(janela, text="Arquivo Salvo!", fg="green", font=fonte_titulo).pack(pady=(20,5))
    print("Arquivo salvo")
    def fechar_janela():
        janela.destroy()

    # Destrói a janela após 1 segundo
    janela.after(1000,fechar_janela)

def adicionar_tarefa(janela_principal: tk.Tk):
    # Criando uma janela de input
    janela = tk.Toplevel(janela_principal)
    janela.title("Input de tarefa")
    centralizar_janela(janela, 400, 250)

    tk.Label(janela, text="Nome da tarefa:", font= fonte_titulo).pack(pady=(20, 5))
    entrada_tarefa = tk.Entry(janela, width=25)
    entrada_tarefa.pack(pady=(0, 10))

    def adicionar():
        tarefa = entrada_tarefa.get().strip()

        if tarefa:
            # Escreve a linha e salva no dataframe
            nova_linha = pd.DataFrame({'Tarefa': [tarefa], 'Status': ['Não Iniciada'], 'Data de Modificação': [strftime('%d/%m/%Y %H:%M:%S', localtime())]})
            janela_principal.df = pd.concat([janela_principal.df, nova_linha], ignore_index=True)
            print(f"Linha: {nova_linha}, adicionada")
            atualizar_frame_direita(janela_principal)
            janela.destroy()
        else:
            tk.Label(janela, text="Digite um nome válido!", fg="red").pack()

    tk.Button(janela, text="Adicionar", command=adicionar).pack(pady=(0, 10))

def atualizar_status(janela_principal: tk.Tk):
    # Criando uma janela de input
    janela = tk.Toplevel(janela_principal)
    janela.title("Input de Status")
    centralizar_janela(janela, 400, 250)

    tk.Label(janela, text="Índice da Tarefa:", font= fonte_titulo).pack(pady=(20, 5))
    entrada_indice = tk.Entry(janela, width=25)
    entrada_indice.pack(pady=(0, 10))
    tk.Label(janela, text="Status:", font= fonte_titulo).pack(pady=(20,5))
    entrada_status = tk.Entry(janela, width= 25)
    entrada_status.pack(pady=(0,10))

    def atualizar():
        indice = entrada_indice.get().strip()
        status = entrada_status.get().strip()
        
        if status and indice:
            try:
                # Altera o status de uma tarefa
                janela_principal.df.loc[int(indice), "Status"] = status
                janela_principal.df.loc[int(indice), 'Data de Modificação'] = strftime('%d/%m/%Y %H:%M:%S', localtime())
                print(f"Status de índice: {indice} atualizado")
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
    centralizar_janela(janela, 400, 250)

    tk.Label(janela, text="Índice da Tarefa:", font= fonte_titulo).pack(pady=(20, 5))
    entrada_indice = tk.Entry(janela, width=25)
    entrada_indice.pack(pady=(0, 10))
    tk.Label(janela, text="Tarefa:", font= fonte_titulo).pack(pady=(20,5))
    entrada_tarefa = tk.Entry(janela, width= 25)
    entrada_tarefa.pack(pady=(0,10))

    def atualizar():
        indice = entrada_indice.get().strip()
        tarefa = entrada_tarefa.get().strip()

        if tarefa and indice:
            try:
                # Altera uma tarefa 
                janela_principal.df.loc[int(indice), "Tarefa"] = tarefa
                janela_principal.df.loc[int(indice), 'Data de Modificação'] = strftime('%d/%m/%Y %H:%M:%S', localtime())
                print(f"Tarefa de índice: {indice} atualizado")
                atualizar_frame_direita(janela_principal)
                janela.destroy()
            except (IndexError, ValueError):
                tk.Label(janela, text="Index inválido!", fg="red").pack()
        else:
            tk.Label(janela, text="Preencha corretamente os campos!", fg="red").pack() 

    tk.Button(janela, text="Atualizar", command=atualizar).pack(pady=(0,10))

def deletar_tarefa(janela_principal: tk.Tk):
    # Criando uma janela de input
    janela = tk.Toplevel(janela_principal)
    janela.title("Input de Índice")
    centralizar_janela(janela, 400, 250)

    tk.Label(janela, text="Índice da Tarefa:", font= fonte_titulo).pack(pady=(20, 5))
    entrada_indice = tk.Entry(janela, width=25)
    entrada_indice.pack(pady=(0, 10))

    def deletar():
        indice = entrada_indice.get().strip()

        if indice:
            try:
                # Deleta uma tarefa
                janela_principal.df.drop(index = int(indice), inplace = True)
                janela_principal.df.reset_index(drop=True, inplace = True)
                print(f"Tarefa de índice: {indice} deletada")
                atualizar_frame_direita(janela_principal)
                janela.destroy()
            except (IndexError, ValueError):
                tk.Label(janela, text="Index Inválido", fg="red").pack()
        else:
            tk.Label(janela, text="Preencha corretamente o campo!", fg="red").pack()
        
    tk.Button(janela, text="Deletar", command=deletar).pack(pady=(0,10))