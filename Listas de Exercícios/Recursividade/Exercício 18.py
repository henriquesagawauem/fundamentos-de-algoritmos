def invert(lst: list[int]) -> list[int]:
    """
    Função que inverte uma lista de inteiros.
    
    >>> invert([1, 2, 3, 4, 5])
    [5, 4, 3, 2, 1]
    >>> invert([1])
    [1]
    >>> invert([])
    []
    """

    resultado = []

    if len(lst) == 0:
        resultado = []
    else:
        resultado = [lst[len(lst) - 1]] + invert(lst[:len(lst) - 1])

    return resultado