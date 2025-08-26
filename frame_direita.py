import tkinter as tk
from auxiliares import fonte_df

def atualizar_frame_direita(janela: tk.Tk):
    frame_direita = janela.frame_direita

    # Limpar conteúdo anterior
    for widget in frame_direita.winfo_children():
        widget.destroy()

    # Criando as colunas
    frame_direita.colunaIndex = tk.Frame(frame_direita, width=200)
    frame_direita.colunaIndex.grid(column=0, row=0, sticky="nsew")

    frame_direita.colunaTarefa = tk.Frame(frame_direita, width=200)
    frame_direita.colunaTarefa.grid(column=1, row=0, sticky="nsew")

    frame_direita.colunaStatus = tk.Frame(frame_direita, width=200)
    frame_direita.colunaStatus.grid(column=2, row=0, sticky="nsew")

    frame_direita.colunaModificacao = tk.Frame(frame_direita, width=200)
    frame_direita.colunaModificacao.grid(column=3, row=0, sticky="nsew")

    frame_direita.grid_columnconfigure(0, weight=1)
    frame_direita.grid_columnconfigure(1, weight=1)
    frame_direita.grid_columnconfigure(2, weight=1)
    frame_direita.grid_columnconfigure(3, weight=1)
    janela.grid_rowconfigure(0, weight=1)

    # Preencher colunas com os dados do DataFrame
    if janela.df is not None and not janela.df.empty:
        # Cabeçalhos
        tk.Label(frame_direita.colunaIndex, text="ID", font=fonte_df).pack(pady=5)
        tk.Label(frame_direita.colunaTarefa, text="Tarefa", font=fonte_df).pack(pady=5)
        tk.Label(frame_direita.colunaStatus, text="Status", font=fonte_df).pack(pady=5)
        tk.Label(frame_direita.colunaModificacao, text="Data de Modificação", font=fonte_df).pack(pady=5)

        # Linhas do DataFrame
        for i, row in janela.df.iterrows():
            tk.Label(frame_direita.colunaIndex, text=str(i), font=fonte_df).pack(pady=2)
            tk.Label(frame_direita.colunaTarefa, text=row["Tarefa"], font=fonte_df).pack(pady=2)
            tk.Label(frame_direita.colunaStatus, text=row["Status"], font=fonte_df).pack(pady=2)
            tk.Label(frame_direita.colunaModificacao, text=row["Data de Modificação"], font=fonte_df).pack(pady=2)

    else:
        aviso = tk.Label(frame_direita, text="Nenhum arquivo selecionado!", font=fonte_df)
        aviso.grid(column=0, row=0, columnspan=4, pady=10)