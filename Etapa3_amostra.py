from rich import console 
from rich.panel import Panel

from rich.table import Table

from Etapa1_carregar import carregar_dados
from Formatacao import console, numero_br

def mostrar_amostra(df, linha=5):

    colunas =["ano","estado", "cidade", "zona", "secao", "cargo", "candidato", "partido", "votos"]

    tabela = Table(title=f"Primeiras {linha} linhas", header_style="bold cyan")

    for coluna in colunas:
        tabela.add_column(coluna)

    for _, registro in df.head(linha).iterrows():
        valores = [str(registro[coluna]) for coluna in colunas]
        tabela.add_row(*valores)
    
    console.print(tabela)   


if __name__ == "__main__":
    df = carregar_dados()
    mostrar_amostra(df)