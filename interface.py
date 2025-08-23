import tkinter as tk
from gerenciar_arquivos import *
from gerenciar_dataframes import *
from auxiliares import *

def janela_principal() -> tk.Tk:
    janela = tk.Tk()
    janela.title("Janela Principal")
    centralizar_janela(janela, 1400, 800)

    # Frames
    frame_esquerda = tk.Frame(janela, bg="yellow", width=400)
    frame_esquerda.grid(row=0, column=0, sticky="nsew")

    frame_direita = tk.Frame(janela, bg="green", width=1000)
    frame_direita.grid(row=0, column=1, sticky="nsew")

    frame_esquerda.grid_columnconfigure(0, minsize=400)
    frame_direita.grid_columnconfigure(0, minsize=1000)

    # Scrollbar no frame direito
    canvas = tk.Canvas(frame_direita)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame_direita, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    frame_scroll = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame_scroll, anchor="nw")

    def ajustar_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame_scroll.bind("<Configure>", ajustar_scroll)

    # Seleção de arquivo
    tk.Button(frame_esquerda, text="Selecionar arquivo", command=lambda: selecionar_arquivo(janela)).pack(pady=10)

    # Criar arquivo
    tk.Button(frame_esquerda, text="Criar arquivo",
              command=lambda: criar_arquivo_csv(janela)).pack(pady=10)

    return janela

if __name__ == "__main__":
    janela = janela_principal()
    janela.mainloop()