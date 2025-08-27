import tkinter as tk
import pandas as pd

# ---Fontes do programa---
fonte_titulo = ("Arial", 20)
fonte_botao = ("Arial", 13)
fonte_df = ("Arial", 12)

def centralizar_janela(janela: tk.Tk, largura: int, altura: int):
    # Conseguindo o tamanho da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Calculando as coordenadas
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)

    # Aplicando as coordenadas
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

def carregar_dataframe(janela_principal: tk.Tk):
    # Leitura do arquivo escolhido e carregando em um dataframe
    janela_principal.df = pd.read_csv(janela_principal.caminho_arquivo, sep=";")
    print("Arquivo carregado")