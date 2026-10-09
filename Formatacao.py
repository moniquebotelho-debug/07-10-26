"""ETAPA DE FORMATAÇÃO DOS MEUS DADOS QUE SERÃO EXIBIDOS"""

from rich.console import Console

console = Console()

def numero_br (valor, casas_decimais=0):
    texto = f"{valor:,.{casas_decimais}f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return texto

    