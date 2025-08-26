import tkinter as tk
from auxiliares import centralizar_janela
from frame_direita import atualizar_frame_direita
from frame_esquerda import atualizar_frame_esquerda

def janela_principal() -> tk.Tk:
    janela = tk.Tk()
    janela.title("Gerenciador de Tarefas")
    centralizar_janela(janela, 1200, 600)

    # atributos globais
    janela.caminho_arquivo = None
    janela.df = None

    # frame esquerda
    janela.frame_esquerda = tk.Frame(janela, width=300, bd=3, relief="solid")
    janela.frame_esquerda.grid(column=0, row=0, sticky="nsew")

    # frame direita
    janela.frame_direita = tk.Frame(janela)
    janela.frame_direita.grid(column=1, row=0, sticky="nsew")

    # ajustes do grid
    janela.grid_columnconfigure(0, minsize=300)
    janela.grid_columnconfigure(1, weight=1)
    janela.grid_rowconfigure(0, weight=1)

    # inicializar interface
    atualizar_frame_esquerda(janela)
    atualizar_frame_direita(janela)

    return janela

if __name__ == "__main__":
    janela = janela_principal()
    janela.mainloop()
