import tkinter as tk
from auxiliares import fonte_titulo

fonte_titulo = ("Arial", 20)

def atualizar_frame_direita(janela: tk.Tk):
    frame_direita = janela.frame_direita

    for widget in frame_direita.winfo_children():
        widget.destroy()

    if janela.df is not None:
        texto_df = tk.Text(frame_direita, wrap="none", font= fonte_titulo)
        texto_df.insert("1.0", janela.df.to_string(index=True))
        texto_df.config(state="disabled")
        texto_df.pack(pady=10)
    else:
        tk.Label(frame_direita, text="Nenhum arquivo selecionado!", font=fonte_titulo).pack(pady=10)
