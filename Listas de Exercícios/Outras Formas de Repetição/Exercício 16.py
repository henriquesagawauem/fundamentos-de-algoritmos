def lista_dobrada(lista: list[int]) -> bool:
    """
    Verifica se *lista* é dobrada

    >>> lista_dobrada([1, 2, 1, 2])
    True
    >>> lista_dobrada([1, 2, 3, 4])
    False
    """

    if len(lista) % 2 != 0:
        return False

    n: int = len(lista) // 2
    i: int = 0
    eh_dobrada = True

    while i < n and eh_dobrada:
        if lista[i] != lista[i + n]:
            eh_dobrada = False

        i = i + 1

    return eh_dobrada
