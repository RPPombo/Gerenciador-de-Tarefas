import pandas as pd
from auxiliares import *
import tkinter as tk

def carregar_dataframe(caminho_arquivo: str, janela_principal: tk.Tk) -> pd.DataFrame:
    # Leitura do arquivo escolhido 
    df = pd.read_csv(caminho_arquivo)

    # Salvamento do dataframe em uma variável dentro da janela principal
    janela_principal.df = df

def salvar_arquivo(caminho_arquivo: str, janela_principal: tk.Tk):
    # Salva o dataframe no arquivo escolhido
    janela_principal.df.to_csv(caminho_arquivo, sep = ";", index = False)

def adicionar_tarefa(janela_principal: tk.Tk) -> pd.DataFrame:
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
            janela.destroy()
        else:
            tk.Label(janela, text="Digite um nome válido!", fg="red").pack()

    tk.Button(janela, text="Adicionar", command=adicionar).pack(pady=(0, 10))

def atualizar_status(df: pd.DataFrame, indice: int, status: str):
    df.loc[indice, "Status"] = [status]

def atualizar_tarefa(df: pd.DataFrame, indice: int, tarefa_atualizada: str):
    df.loc[indice, "Tarefa"] = [tarefa_atualizada]
