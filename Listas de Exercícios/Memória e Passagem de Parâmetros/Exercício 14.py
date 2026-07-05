def remove(lista: list[int], indice: int) -> None:
    """
    Remove um elemento de uma posição específica da lista.

    Exemplos
    >>> lista = [1, 2, 3, 4, 5]
    >>> remove(lista, 2)
    >>> lista
    [1, 2, 4, 5]
    """
    
    for i in range(indice, len(lista) - 1):
        lista[i] = lista[i + 1]
    
    lista.pop()