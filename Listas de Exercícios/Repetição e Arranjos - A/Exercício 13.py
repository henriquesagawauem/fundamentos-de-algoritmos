def pares(lista: list[int]) -> bool:
    """
    Verifica se todos os elementos de uma lista de inteiros
    são pares

    Exemplos
    >>> pares([1, 2, 3])
    False
    >>> pares([2, 4, 6])
    True
    """

    pares: bool = True
    i: int = 0

    while i < len(lista) and pares:
        if lista[i] % 2 != 0:
            pares = False
        i = i + 1

    return pares
