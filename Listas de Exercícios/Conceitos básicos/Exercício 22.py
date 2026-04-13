# Projete uma função que verifique se o caractere do meio de uma string é '-'.

# ----------------------------------------------------------------------------------------------

# Análise
# Verificar se o caractere do meio de uma string é '-'
#
# Tipos de dados
# uma string

def caractere_meio(s: str) -> bool:
    """
    Retorna True se o caractere do meio de *s* for '-'

    Exemplos
    >>> caractere_meio("1-2")
    True
    >>> caractere_meio("fern-ando")
    True
    >>> caractere_meio("fer-nando")
    False
    >>> caractere_meio("fernando")
    False
    >>> caractere_meio("-")
    True
    """
    return s[(len(s) - 1) // 2] == "-"