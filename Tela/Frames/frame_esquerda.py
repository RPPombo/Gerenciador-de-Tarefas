import tkinter as tk
from tkinter import filedialog
from Serviços.auxiliares import *
from Tela.Frames.frame_direita import atualizar_frame_direita
from Serviços.gerenciar_dataframes import *

def atualizar_frame_esquerda(janela: tk.Tk):
    frame_esquerda = janela.frame_esquerda

    # Limpando o conteúdo anterior
    for widget in frame_esquerda.winfo_children():
        widget.destroy()

    # Criando os botões de ação
    tk.Label(frame_esquerda, text="Arquivos", font=fonte_titulo).pack(pady=10)

    tk.Button(frame_esquerda, text="Selecionar arquivo", font=fonte_botao,command=lambda: selecionar_arquivo(janela)).pack(pady=10)

    tk.Button(frame_esquerda, text="Criar arquivo", font=fonte_botao,command=lambda: criar_arquivo_csv(janela)).pack(pady=10)

    # Botões que aparecem somente quando arquivo é carregado
    if janela.caminho_arquivo:
        tk.Button(frame_esquerda, text="Salvar Arquivo", font=fonte_botao,
                  command=lambda: salvar_arquivo(janela)).pack(pady=10)

        tk.Label(frame_esquerda, text="Tarefas", font=fonte_titulo).pack(pady=10)

        tk.Button(frame_esquerda, text="Adicionar Tarefa", font=fonte_botao,command=lambda: adicionar_tarefa(janela)).pack(pady=10)

        tk.Button(frame_esquerda, text="Atualizar Status", font=fonte_botao,command=lambda: atualizar_status(janela)).pack(pady=10)

        tk.Button(frame_esquerda, text="Atualizar Tarefa", font=fonte_botao,command=lambda: atualizar_tarefa(janela)).pack(pady=10)
        
        tk.Button(frame_esquerda, text="Deletar Tarefa", font=fonte_botao, command=lambda: deletar_tarefa(janela)).pack(pady=(10))

    print("Frame esquerda carregado")

# ---Botões de Carregamento de arquivo---
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
        print("Arquivo Selecionado")
        carregar_dataframe(janela_principal)
        atualizar_frame_esquerda(janela_principal)
        atualizar_frame_direita(janela_principal)
        


def criar_arquivo_csv(janela_principal: tk.Tk):
    # Abre o seletor de diretório na pasta Documents
    diretorio = filedialog.askdirectory(
        parent=janela_principal,
        initialdir="C:/Documents",
        title="Selecione um diretório"
    )

    if diretorio:
        # Criando janela de criação de arquivo
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
                    arquivo.write("Tarefa;Status;Data de Modificação\n")

                # Salva como atributo da janela principal
                janela_principal.caminho_arquivo = caminho
                print("Arquivo criado")
                carregar_dataframe(janela_principal)
                atualizar_frame_esquerda(janela_principal)
                atualizar_frame_direita(janela_principal)
                janela.destroy()
            else:
                tk.Label(janela, text="Digite um nome válido!", fg="red").pack()

        tk.Button(janela, text="Criar", command=criar).pack(pady=(0, 10))