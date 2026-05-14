def lista_par(l: list[int]) -> list[int]:
    """
    Retorna uma lista com os elementos em índices pares de *l*

    Exemplos
    >>> lista_par([1, 2, 3, 4, 5, 6, 7, 8])
    [1, 3, 5, 7]
    """

    nova = []

    for i in range(len(l)):
        if i % 2 == 0:
            nova.append(l[i])

    return nova