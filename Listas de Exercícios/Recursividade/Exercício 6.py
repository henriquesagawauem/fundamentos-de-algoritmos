def repete(n: int, v: int) -> list[int]:
    """
    Cria uma nova lista com *n* repetições do valor *v*.

    Exemplos
    >>> repete(3, 5)
    [5, 5, 5]
    """

    lista: list[int] = []

    if n == 0:
        lista = []
    else:
        lista.append(v)
        lista = lista + repete(n - 1, v)

    return lista