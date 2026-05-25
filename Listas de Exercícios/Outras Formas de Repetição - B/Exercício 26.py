def soma_zero(matriz: list[list[int]]) -> list[int]:
    """
    Encontra o índice de uma coluna na qual a soma dos elementos é zero

    Exemplos
    >>> soma_zero([[0, 1], [0, 2], [0, 3]])
    [0]
    """

    indices = []

    num_colunas = len(matriz[0])

    for i in range(num_colunas):
        soma = 0
        for j in range(len(matriz)):
            soma = soma + matriz[j][i]

        if soma == 0:
            indices.append(i)

    return indices
