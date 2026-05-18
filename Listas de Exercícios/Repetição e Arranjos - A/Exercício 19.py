def menor_num(lista: list[int]) -> int:
    """
    Retorna o menor valor de uma lista de inteiros
    """

    menor: int = lista[0]

    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]

    return menor


def normaliza(lista: list[int]) -> list[int]:
    """
    Normaliza os valores de *lista*

    >>> normaliza([5, 2, 8, 3])
    [3, 0, 6, 1]
    """

    menor: int = menor_num(lista)

    for i in range(len(lista)):
        lista[i] = lista[i] - menor

    return lista