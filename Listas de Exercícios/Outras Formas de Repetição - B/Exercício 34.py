def estacao(m: list[list[float]]) -> list[int]:
    """
    Exemplos:
    >>> estacao([[-2, -2], [-2, -1]])
    [[1, 1]]
    >>> estacao([[-1, -2, -3], [-1, -2, -1], [2, -1, -7]])
    [[2, 0]]
    """

    imax = 0
    jmax = 0

    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] > m[imax][jmax]:
                imax = i
                jmax = j

    return [imax, jmax]