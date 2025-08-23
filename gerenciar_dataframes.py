import pandas as pd

def carregar_arquivo(caminho_arquivo: str) -> pd.DataFrame:
    df = pd.read_csv(caminho_arquivo)
    return df

def salvar_arquivo(caminho_arquivo: str, df: pd.DataFrame):
    df.to_csv(caminho_arquivo, sep = ";", index = False)


def escrever_tarefa(df: pd.DataFrame, tarefa: str) -> pd.DataFrame:
    nova_linha = pd.DataFrame({'Tarefa':[tarefa], 'Status':['Não Iniciada']})
    return pd.concat([df, nova_linha], ignore_index= True)

def atualizar_status(df: pd.DataFrame, indice: int, status: str):
    df.loc[indice, "Status"] = [status]

def atualizar_tarefa(df: pd.DataFrame, indice: int, tarefa_atualizada: str):
    df.loc[indice, "Tarefa"]
