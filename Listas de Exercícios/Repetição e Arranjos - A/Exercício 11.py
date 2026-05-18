def str_int(lista: list[str]) -> list[int]:
    """
    Transforma todas as string de *lista* em uma
    lista de inteiros

    Exemplos
    >>> str_int(['1', '2', '3'])
    [1, 2, 3]
    """

    lista_int: list[int] = []

    for i in lista:
        lista_int.append(int(i))

    return lista_int
