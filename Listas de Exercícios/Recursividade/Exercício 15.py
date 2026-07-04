def lista_pos(lista: list[int]) -> list[int]:
    """
    Retorna uma lista contendo apenas os números positivos de *lista*.

    Exemplos
    >>> lista_pos([1, -1, -2, -1, 2, 3])
    [1, 2, 3]
    >>> lista_pos([-1, -2, -1])
    []
    >>> lista_pos([1, 2, 3])
    [1, 2, 3]
    """

    lista_auxiliar = []

    if len(lista) >= 1:
        if lista[0] > 0:
            lista_auxiliar.append(lista[0])

        lista_auxiliar = lista_auxiliar + lista_pos(lista[1:])

    return lista_auxiliar
