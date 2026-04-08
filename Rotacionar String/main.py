def rotacionar_string(string: str, n: int) -> str:
    """
    Rotaciona uma string n posições a direita. Isto é, significa mover os últimos
    n caracteres de uma string para as n primeiras posições da string

    Exemplos
    >>> rotacionar_string("marcelio", 5)
    'celiomar'
    >>> rotacionar_string("fernando", 3)
    'ndoferna'
    """
    return f"{string[-n:]}{string[0:-n]}"