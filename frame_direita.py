import tkinter as tk
from auxiliares import fonte_df

def atualizar_frame_direita(janela: tk.Tk):
    frame_direita = janela.frame_direita

    # Limpar conteúdo anterior
    for widget in frame_direita.winfo_children():
        widget.destroy()

    # Criar canvas e scrollbar
    canvas = tk.Canvas(frame_direita)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(frame_direita, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    # Frame interno que vai conter as colunas
    frame_interno = tk.Frame(canvas)
    window_id = canvas.create_window((0, 0), window=frame_interno, anchor="nw")

    # Atualiza scrollregion e largura do frame interno
    def ajustar_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
        canvas.itemconfig(window_id, width=canvas.winfo_width())  # expande horizontalmente

    frame_interno.bind("<Configure>", ajustar_scroll)

    # Criando as colunas dentro do frame interno
    colunaIndex = tk.Frame(frame_interno, width=200)
    colunaIndex.grid(column=0, row=0, sticky="nsew")

    colunaTarefa = tk.Frame(frame_interno, width=200)
    colunaTarefa.grid(column=1, row=0, sticky="nsew")

    colunaStatus = tk.Frame(frame_interno, width=200)
    colunaStatus.grid(column=2, row=0, sticky="nsew")

    colunaModificacao = tk.Frame(frame_interno, width=200)
    colunaModificacao.grid(column=3, row=0, sticky="nsew")

    # Configura colunas para expandirem igualmente
    for i in range(4):
        frame_interno.grid_columnconfigure(i, weight=1)

    # Preencher colunas com dados
    if janela.df is not None and not janela.df.empty:
        tk.Label(colunaIndex, text="ID", font=fonte_df).pack(pady=5)
        tk.Label(colunaTarefa, text="Tarefa", font=fonte_df).pack(pady=5)
        tk.Label(colunaStatus, text="Status", font=fonte_df).pack(pady=5)
        tk.Label(colunaModificacao, text="Data de Modificação", font=fonte_df).pack(pady=5)

        for i, row in janela.df.iterrows():
            tk.Label(colunaIndex, text=str(i), font=fonte_df).pack(pady=2)
            tk.Label(colunaTarefa, text=row["Tarefa"], font=fonte_df).pack(pady=2)
            tk.Label(colunaStatus, text=row["Status"], font=fonte_df).pack(pady=2)
            tk.Label(colunaModificacao, text=row["Data de Modificação"], font=fonte_df).pack(pady=2)  
    elif janela.df is not None and janela.df.empty:
        tk.Label(frame_interno, text="Nenhum dado presente!", font=fonte_df).grid(column=0, row=0, columnspan=4, pady=10)
    else:
        tk.Label(frame_interno, text="Nenhum arquivo carregado!", font=fonte_df).grid(column=0, row=0, columnspan=4, pady=10)

    print("Frame direita carregado")
