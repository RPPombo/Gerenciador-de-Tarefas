import pandas as pd

def escrever_tarefa(df: pd.DataFrame, tarefa: str) -> pd.DataFrame:
    nova_linha = pd.DataFrame({'Tarefa':[tarefa], 'Status':['Não Iniciada']})
    return pd.concat([df, nova_linha], ignore_index= True)

def atualizar_status(df: pd.DataFrame, indice: int, status: str):
    df.loc[indice, "Status"] = [status]

def atualizar_tarefa(df: pd.DataFrame, indice: int, tarefa_atualizada: str):
    df.loc[indice, "Tarefa"]
