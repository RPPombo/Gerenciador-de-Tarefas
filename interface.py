import tkinter as tk
from auxiliares import *
from gerenciar_dataframes import *
from gerenciar_arquivos import *

fonte_titulo = ("Arial", 20)
fonte_botao = ("Arial", 13)

def atualizar_frame_esquerda(janela: tk.Tk):
    frame_esquerda = janela.frame_esquerda

    # Limpar frame
    for widget in frame_esquerda.winfo_children():
        widget.destroy()

    # Recriar interface
    tk.Label(frame_esquerda, text="Arquivos", font= fonte_titulo).pack(pady=10)
    tk.Button(frame_esquerda, text="Selecionar arquivo",font= fonte_botao, command=lambda: selecionar_arquivo(janela)).pack(pady=10)
    tk.Button(frame_esquerda, text="Criar arquivo",font= fonte_botao, command=lambda: criar_arquivo_csv(janela)).pack(pady=10)

    # Só aparece se houver caminho de arquivo válido
    if janela.caminho_arquivo:
        tk.Button(frame_esquerda, text="Salvar Arquivo", font=fonte_botao, command=salvar_arquivo(janela)).pack(pady=10)

        tk.Label(frame_esquerda, text="Tarefas", font= fonte_titulo).pack(pady=10)

        tk.Button(frame_esquerda, text="Adicionar Tarefa",font= fonte_botao,command=lambda: adicionar_tarefa(janela)).pack(pady=10)

        tk.Button(frame_esquerda, text="Atualizar Status", font= fonte_botao, command= lambda: atualizar_status(janela)).pack(pady=10)

        tk.Button(frame_esquerda, text="Atualizar Tarefa", font=fonte_botao, command=lambda: atualizar_tarefa(janela)).pack(pady=10)


def janela_principal() -> tk.Tk:
    janela = tk.Tk()
    janela.title("Janela Principal")
    centralizar_janela(janela, 1200, 600)

    janela.caminho_arquivo = None

    # Criar frames
    janela.frame_esquerda = tk.Frame(janela, bg="yellow", width=300)
    janela.frame_esquerda.grid(column=0, row=0, sticky="nsew")

    frame_direita = tk.Frame(janela, bg="green")
    frame_direita.grid(column=1, row=0, sticky="nsew")

    janela.grid_columnconfigure(0, minsize=300)
    janela.grid_columnconfigure(1, weight=1)
    janela.grid_rowconfigure(0, weight=1)

    # Inicializa menu lateral
    atualizar_frame_esquerda(janela)
        
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