def insere_elemento(lista: list[int], elemento: int, indice: int) -> None:
    """
    Insere um elemento em uma posição específica da lista.

    Exemplos
    >>> lista = [1, 2, 3, 4, 5]
    >>> insere_elemento(lista, 10, 2)
    >>> lista
    [1, 2, 10, 3, 4, 5]
    """

    lista.append(elemento)

    for i in range(len(lista) - 1, indice, -1):
        lista[i] = lista[i - 1]

    lista[indice] = elemento