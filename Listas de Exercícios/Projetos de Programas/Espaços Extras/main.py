# Análise
# Verificar se o texto enviado pelo usuário está dentro da regra
# de formataçãom, sem espaços em branco no começo e no fim
#
# Tipos de dados
# Texto digitado pelo usuário

def espacos_extras(text: str) -> bool:
    """
    Verifica o texto enviado pelo usuário, seguindo uma regra específica,
    o texto não deve conter espaços extras, ou seja, espaços em brancos
    no final e no ínicio do texto, caso não esteja de acordo com as regras
    retorna False, caso contrário retorna True

    Exemplos
    >>> espacos_extras("Meu texto")
    True
    >>> espacos_extras(" Meu texto errado")
    False
    >>> espacos_extras("Meu texto errado 2 ")
    False
    >>> espacos_extras(" Meu texto errado 3 ")
    False
    >>> espacos_extras("Meu texto certo 4")
    True
    """
    return text[0] != " " and text[len(text) - 1] != " "
