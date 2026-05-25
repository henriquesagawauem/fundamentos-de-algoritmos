def eh_simetrica(m: list[list[int]]) -> bool:
    """
    Verifica se uma matriz é simétrica.

    Exemplos
    >>> eh_simetrica([[1, 2], [2, 1]])
    True
    >>> eh_simetrica([[1, 2], [3, 1]])
    False
    >>> eh_simetrica([[1, 2, 3], [2, 4, 5], [3, 5, 6]])
    True
    >>> eh_simetrica([[1, 2], [2, 3], [3, 4]])
    False
    """
    existe = True

    if len(m) != len(m[0]):
        existe = False

    if existe:
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] != m[j][i]:
                    existe = False

    return existe
