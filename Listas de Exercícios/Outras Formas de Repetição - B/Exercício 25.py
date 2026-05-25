def soma_zero(matriz: list[list[int]]) -> list[int]:
    """
    Encontra o índice de linhas na qual a soma dos elementos é zero

    Exemplos
    >>> soma_zero([[1, -1], [0, 3], [0, 0]])
    [0, 2]
    """

    indices = []

    for i in range(len(matriz)):
        soma = 0
        for j in range(len(matriz[i])):
            soma = soma + matriz[i][j]

        if soma == 0:
            indices.append(i)

    return indices
