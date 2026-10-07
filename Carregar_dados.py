"""ETAPA 01: LER O ARQUIVO CSV COM OS DADOS DA ELEIÇÃO"""

import pandas as pd

CAMINHO_CSV = "Eleicoes.csv"

def carregar_dados():
    df = pd.read_csv(CAMINHO_CSV, dtype={"zona": str, "secao": str})
    return df

if __name__ == "__main__":
    df = carregar_dados()
    print(df.head())