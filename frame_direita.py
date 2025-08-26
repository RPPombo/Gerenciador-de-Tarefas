import tkinter as tk
from auxiliares import fonte_titulo

fonte_titulo = ("Arial", 20)

def atualizar_frame_direita(janela: tk.Tk):
    frame_direita = janela.frame_direita

    # Limpar conteúdo anterior
    for widget in frame_direita.winfo_children():
        widget.destroy()

    # Criando as colunas
    frame_direita.colunaIndex = tk.Frame(frame_direita, bg="brown", width=200)
    frame_direita.colunaIndex.grid(column=0, row=0, sticky="nsew")

    frame_direita.colunaTarefa = tk.Frame(frame_direita, bg="brown", width=200)
    frame_direita.colunaTarefa.grid(column=1, row=0, sticky="nsew")

    frame_direita.colunaStatus = tk.Frame(frame_direita, bg="brown", width=200)
    frame_direita.colunaStatus.grid(column=2, row=0, sticky="nsew")

    frame_direita.colunaModificacao = tk.Frame(frame_direita, bg="brown", width=200)
    frame_direita.colunaModificacao.grid(column=3, row=0, sticky="nsew")

    frame_direita.grid_columnconfigure(0, weight=1)
    frame_direita.grid_columnconfigure(1, weight=1)
    frame_direita.grid_columnconfigure(2, weight=1)
    frame_direita.grid_columnconfigure(3, weight=1)
    janela.grid_rowconfigure(0, weight=1)

    # Preencher colunas com os dados do DataFrame
    if janela.df is not None and not janela.df.empty:
        # Cabeçalhos
        tk.Label(frame_direita.colunaIndex, text="ID", font=("Arial", 12, "bold")).pack(pady=5)
        tk.Label(frame_direita.colunaTarefa, text="Tarefa", font=("Arial", 12, "bold")).pack(pady=5)
        tk.Label(frame_direita.colunaStatus, text="Status", font=("Arial", 12, "bold")).pack(pady=5)
        tk.Label(frame_direita.colunaModificacao, text="Ações", font=("Arial", 12, "bold")).pack(pady=5)

        # Linhas do DataFrame
        for i, row in janela.df.iterrows():
            tk.Label(frame_direita.colunaIndex, text=str(i)).pack(pady=2)
            tk.Label(frame_direita.colunaTarefa, text=row["Tarefa"]).pack(pady=2)
            tk.Label(frame_direita.colunaStatus, text=row["Status"]).pack(pady=2)
            tk.Label(frame_direita.colunaModificacao, text=row["Data de Modificação"]).pack(pady=2)

    else:
        aviso = tk.Label(frame_direita, text="Nenhum arquivo selecionado!", font=fonte_titulo)
        aviso.grid(column=0, row=0, columnspan=4, pady=10)