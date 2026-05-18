def del_zero(lista: list[int]) -> list[int]:
    """
    Remove todos os elementos 0 de *lista*

    Exemplos
    >>> del_zero([1, 2, 3, 0])
    [1, 2, 3]
    >>> del_zero([0, 0, 0, 0])
    []
    >>> del_zero([1, 0, 2, 0, 3, 0])
    [1, 2, 3]
    """

    nova_lista: list[int] = []

    for i in lista:
        if i != 0:
            nova_lista.append(i)

    return nova_lista