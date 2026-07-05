def remove_par(lista: list[int]) -> None:
    """
    Remove todos os elementos pares de *lista*

    Exemplos
    >>> lista = [1, 2, 3, 4]
    >>> remove_par(lista)
    >>> lista
    [1, 3]
    """
    for i in range(len(lista) - 1):
        if lista[i] % 2 == 0:
            for i in range(i, len(lista) - 1):
                lista[i] = lista[i + 1]
    
            lista.pop()
