import tkinter as tk
from tkinter import filedialog
import pandas as pd

def selecionar_arquivo() -> str:
    # Cria a janela principal "oculta"
    janela = tk.Tk()
    janela.withdraw()

    # Abre o seletor de arquivos na pasta Documents
    caminho_arquivo = filedialog.askopenfilename(
        initialdir="C:/Documents",  
        title="Selecione um arquivo CSV",
        filetypes=(("Arquivos CSV", "*.csv"), ("Todos os arquivos", "*.*"))
    )

    return caminho_arquivo

def criar_arquivo_csv(nome_arquivo: str) -> str:
    # Cria a janela principal "oculta"
    janela = tk.Tk()
    janela.withdraw()

    # Abre o seletor de diretório na pasta Documents
    diretorio = filedialog.askdirectory(
        initialdir= "C:/Documents",
        title= "Selecione um diretório")
    with open(f"{diretorio}/{nome_arquivo}", "x", encoding = "UTF-8") as arquivo:
        arquivo.write("Tarefa; Status")

    return f"{diretorio}/{nome_arquivo}"

def carregar_arquivo(caminho_arquivo: str):
    df = pd.read_csv(caminho_arquivo)
    return df