def organiza(lista: list[int]) -> list[int]:
    """
    Separa negativos e positivos de *lista*

    Exemplos
    >>> organiza([-2, 3, 4, 5, -2, 3, -1, -23])
    [-2, -2, -1, -23, 3, 4, 5, 3]
    """

    negativos: list[int] = []
    positivos: list[int] = []

    for i in lista:
        if i < 0:
            negativos.append(i)
        else:
            positivos.append(i)

    return negativos + positivos
