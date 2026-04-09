# Análise
# Rotacionar um string. Uma rotação de string se por mover os últimos
# n caracteres de um string para as n primeiras posições da string
#
# Tipos de dados
# uma palavra qualquer com pelo menos 1 caractere


def rotacionar_string(string: str, n: int) -> str:
    """
    Rotaciona uma string n posições a direita, movendo os últimos
    n caracteres de uma string para as n primeiras posições da string

    Exemplos
    >>> rotacionar_string("marcelio", 5)
    'celiomar'
    >>> rotacionar_string("fernando", 3)
    'ndoferna'
    >>> rotacionar_string("a", 4)
    'a'
    """
    return f"{string[-n:]}{string[0:-n]}"
