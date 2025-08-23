import tkinter as tk
from tkinter import filedialog
from auxiliares import *

def selecionar_arquivo(janela_principal: tk.Tk):
    # Abre o seletor de arquivos usando a janela principal como parent
    caminho_arquivo = filedialog.askopenfilename(
        parent=janela_principal,
        initialdir="C:/Documents",
        title="Selecione um arquivo CSV",
        filetypes=(("Arquivos CSV", "*.csv"), ("Todos os arquivos", "*.*"))
    )
    if caminho_arquivo:
        janela_principal.caminho_arquivo = caminho_arquivo


def criar_arquivo_csv(janela_principal:tk.Tk):
    # Abre o seletor de diretório na pasta Documents
    diretorio = filedialog.askdirectory(
        parent=janela_principal,
        initialdir= "C:/Documents",
        title= "Selecione um diretório")

    if diretorio:
        janela = tk.Toplevel(janela_principal)
        janela.title("Input do nome")
        centralizar_janela(janela, 400, 200)

        tk.Label(janela, text="Nome do arquivo:").pack(pady=(20, 5))
        entrada_nome = tk.Entry(janela, width=25)
        entrada_nome.pack(pady=(0, 10))

        with open(f"{diretorio}/{entrada_nome}.csv", "x", encoding = "UTF-8") as arquivo:
            arquivo.write("Tarefa;Status")

        janela_principal.caminho_arquivo = f"{diretorio}/{entrada_nome}.csv"

