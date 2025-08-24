import tkinter as tk
from gerenciar_arquivos import *
from gerenciar_dataframes import *
from auxiliares import *

def janela_principal() -> tk.Tk:
    janela = tk.Tk()
    janela.title("Janela Principal")
    centralizar_janela(janela, 1400, 800)

    # Frames
    frame_esquerda = tk.Frame(janela, bg="yellow", width=400, height=800)
    frame_esquerda.grid(column=0, sticky="nsew")

    frame_direita = tk.Frame(janela, bg="green", width=1000)
    frame_direita.grid(column=1, sticky="nsew")

    janela.grid_columnconfigure(0, minsize=400)
    janela.grid_columnconfigure(1, minsize=1000)

    # Frame Esquerdo
    tk.Label(frame_esquerda, text="Arquivos").pack(pady=10)

    # Seleção de arquivo
    tk.Button(frame_esquerda, text="Selecionar arquivo", command=lambda: selecionar_arquivo(janela)).pack(pady=10)

    # Criação de arquivo
    tk.Button(frame_esquerda, text="Criar arquivo", command=lambda: criar_arquivo_csv(janela)).pack(pady=10)
    
    tk.Label(frame_esquerda, text="Tarefas").pack(pady=10)

    # Adição de tarefa
    tk.Button(frame_esquerda, text="Adicionar Tarefa", command=lambda: adicionar_tarefa(janela)).pack(pady=10)
    
    # Frame Direito
    # Scrollbar
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

    return janela

if __name__ == "__main__":
    janela = janela_principal()
    janela.mainloop()