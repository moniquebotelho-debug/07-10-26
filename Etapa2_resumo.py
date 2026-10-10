from rich import console 
from rich.panel import Panel

from Etapa1_carregar import carregar_dados
from Formatacao import console, numero_br

"""FUNÇÕES: def = cria uma função; df = dataframe (é uma estrutura em formato de tabela, lembra um excel); len = lê quantas linhas tem no datafreme; sum = soma itens; nunique: conta o nº de valores únicos; bold: imprime o texto em negrito"""

def mostrar_resultado(df):
    total_registros = len(df)
    total_votos = df["votos"].sum()
    total_cidades = df["cidade"].nunique()
    total_candidatos = df["candidato"].nunique() 

    texto =(

        f"[bold] Registros: [/] { numero_br(total_registros)}\n"
        f"[bold] Votos: [/] { numero_br(total_votos)}\n"
        f"[bold] Cidades: [/] { numero_br(total_cidades)}\n"
        f"[bold] Candidatos: [/] { numero_br(total_candidatos)}\n"
    )

    console.print(Panel(texto, title="Monique Painel de Eleições", expand=False))

if __name__ == "__main__":
    df  = carregar_dados()
    mostrar_resultado(df)

