def novo_item(lista: list[int], pos: int, item: int) -> list[int]:
    """
    Retorna uma nova lista com o elemento *item*, na posição *pos* em *lista*

    Exemplos
    >>> novo_item([1, 2], 1, 3)
    [1, 3, 2]
    """

    nova_lista: list[int] = []

    for i in range(len(lista)):
        if i == pos:
            nova_lista.append(item)

        nova_lista.append(lista[i])

    return nova_lista
