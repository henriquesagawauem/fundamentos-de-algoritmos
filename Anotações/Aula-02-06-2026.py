def insere_ordenado(lst: list[int], v: int) -> None:
    """
    Insere *v* em *lst* de maneira que *lst*
    permaneça em ordem não decrescente. Requer
    que *lst* esteja em ordem não decrescente.

    Exemplos
    >>> lst = []
    >>> insere_ordenado(lst, 7)
    [7]
    >>> insere_ordenado(lst, 3)
    [3, 7]
    >>> insere_ordenado(lst, 5)
    [3, 5, 7]
    >>> insere_ordenado(lst, 4)
    [3, 4, 5, 7]
    """

    temp = []
    inserido = False

    for i in lst:
        if not inserido and v <= i:
            temp.append(v)
            inserido = True

        temp.append(i)

    if not inserido:
        temp.append(v)

    lst[:] = temp