def remove_pares(lista: list[int]) -> None:
    """
    Remove todos os elementos em índices pares de *lista*

    Exemplos
    >>> lst = [1, 2, 3, 4, 5, 6]
    >>> remove_pares(lst)
    >>> lst
    [2, 4, 6]
    """

    i = len(lista) - 1

    while i >= 0:
        if i % 2 == 0:
            j = i
            while j < len(lista) - 1:
                lista[j] = lista[j + 1]
                j += 1
            lista.pop()
        i -= 1
