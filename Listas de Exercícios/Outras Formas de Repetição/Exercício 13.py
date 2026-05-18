def rotacionar(lista: list[int], n: int) -> list[int]:
    """
    Rotaciona a lista *lista* em *n* posições

    Exemplos
    >>> rotacionar([5, 3, 4, 1, 7], 2)
    [4, 1, 7, 5, 3]
    """

    nova_lista: list[int] = []

    for i in lista[n:]:
        nova_lista.append(i)

    for i in lista[:n]:
        nova_lista.append(i)

    return nova_lista
