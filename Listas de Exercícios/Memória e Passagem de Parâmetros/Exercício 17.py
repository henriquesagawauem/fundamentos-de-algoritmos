def neg_antes(lista: list[int]) -> None:
    """
    Coloca os valores negativos antes dos valores positivos, mantendo a ordem relativa entre eles.

    Exemplos
    >>> lista = [1, -2, 3, -4, 5]
    >>> neg_antes(lista)
    >>> lista
    [-2, -4, 1, 3, 5]

    >>> lista = [-1, 2, -2]
    >>> neg_antes(lista)
    >>> lista
    [-1, -2, 2]
    """

    i = 0
    while i < len(lista):
        if lista[i] < 0:
            j = i
            while j > 0 and lista[j - 1] > 0:
                temp = lista[j]
                lista[j] = lista[j - 1]
                lista[j - 1] = temp

                j -= 1
        i += 1