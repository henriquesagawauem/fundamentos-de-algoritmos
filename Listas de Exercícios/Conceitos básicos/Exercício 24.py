# 24) Quando escrevemos uma data no Brasil em geral usamos a ordem dia/mês/ano. Já em outros países a
# ordem usada é mês/dia/ano. Uma outra forma mais recente de escrever a data é ano/mês/dia. Projete
# uma função que receba como entrada o dia, o mês e o ano e gere uma string representando a data na
# forma ano/mês/dia.

# -------------------------------------------------------------------------------------------------------

# Análise
# Transformar a data no formato "dia/mes/ano" no formato "ano/mes/dia"
#
# Tipos de dados
# Data no formato "dia/mes/ano" onde da e mes tem dois dígitos e ano tem quatro dígitos


def dma_para_amd(data: str) -> str:
    """
    Transforma *data*, que deve estar no formato "dia/mes/ano",
    onde dia e mes tem dois dígitos e ano tem quatro dígitos,
    para o formato "ano/mes/dia".

    Exemplos
    >>> dma_para_amd("15/05/2005")
    '2005/05/15'
    >>> dma_para_amd("26/08/1914")
    '1914/08/26'
    """
    return f"{data[6:]}/{data[3:5]}/{data[:2]}"