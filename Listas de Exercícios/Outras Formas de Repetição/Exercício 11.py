def del_element(lista: list[int], pos: int) -> list[int]:
    """
    Retorna uma lista, mas sem o elemento na posição *pos* em *lista*

    Exemplos
    >>> del_element([1, 2, 3], 1)
    [1, 3]
    >>> del_element([1, 2, 3, 4, 5, 6], 4)
    [1, 2, 3, 4, 6]
    """

    nova_lista: list[int] = []

    for i in range(len(lista)):
        if i != pos:
            nova_lista.append(lista[i])

    return nova_lista
