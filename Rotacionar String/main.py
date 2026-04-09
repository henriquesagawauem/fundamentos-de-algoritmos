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
    >>> rotacionar_string("abapiru", 2)
    'ruabapi'
    """
    return f"{string[len(string) - n :]}{string[0 : len(string) - n]}"
