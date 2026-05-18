def produto(lista: list[int]) -> int:
    """
    Calcula o produto de todos os elementos de *lista*

    Exemplos
    >>> produto([2, 2, 2])
    8
    """

    produto: int = 1

    for i in lista:
        produto = produto * i

    return produto
