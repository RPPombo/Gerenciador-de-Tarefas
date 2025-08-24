import tkinter as tk
from tkinter import filedialog
from auxiliares import *
from interface import atualizar_frame_esquerda

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
        atualizar_frame_esquerda(janela_principal)


def criar_arquivo_csv(janela_principal: tk.Tk):
    # Abre o seletor de diretório na pasta Documents
    diretorio = filedialog.askdirectory(
        parent=janela_principal,
        initialdir="C:/Documents",
        title="Selecione um diretório"
    )

    if diretorio:
        janela = tk.Toplevel(janela_principal)
        janela.title("Input do nome")
        centralizar_janela(janela, 400, 200)

        tk.Label(janela, text="Nome do arquivo:").pack(pady=(20, 5))
        entrada_nome = tk.Entry(janela, width=25)
        entrada_nome.pack(pady=(0, 10))

        def criar():
            nome = entrada_nome.get().strip()
            if nome:
                caminho = f"{diretorio}/{nome}.csv"
                with open(caminho, "x", encoding="UTF-8") as arquivo:
                    arquivo.write("Tarefa;Status\n")

                # salva como atributo da janela principal
                janela_principal.caminho_arquivo = caminho
                atualizar_frame_esquerda(janela_principal)
                janela.destroy()
            else:
                tk.Label(janela, text="Digite um nome válido!", fg="red").pack()

        tk.Button(janela, text="Criar", command=criar).pack(pady=(0, 10))
        

