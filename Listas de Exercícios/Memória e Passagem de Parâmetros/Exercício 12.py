def junta_lista(lista1: list[int], lista2: list[int]) -> list[int]:
    """
    Junta duas listas de inteiros em uma só.

    Exemplos
    >>> junta_lista([1, 2, 3], [4, 5, 6])
    [1, 2, 3, 4, 5, 6]
    >>> junta_lista([1, 2], [3])
    [1, 2, 3]
    """
    
    for i in lista2:
        lista1.append(i)
    
    return lista1