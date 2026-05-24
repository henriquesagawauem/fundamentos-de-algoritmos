def matriz_identidade(n: int) -> list[list[int]]:
    """
    Criar uma matriz identidade com *n* linhas e *n* colunas

    Exemplos
    >>> matriz_identidade(4)
    [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    >>> matriz_identidade(0)
    []
    """
    matriz: list[list[int]] = []
    for i in range(n):
        lista = []
        for j in range(n):
            if j == i:
                lista.append(1)
            else:
                lista.append(0)
        matriz.append(lista)
    return matriz
