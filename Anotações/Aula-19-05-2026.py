def cria_matriz_nula(m: int, n: int) -> list[list[int]]:
    """
    Cria uma matriz nula com *m* linhas e *n* colunas.
    Requer que m > 0 e n > 0.
    Exemplos
    >>> cria_matriz_nula(2, 3)
    [[0, 0, 0], [0, 0, 0]]

    >>> cria_matriz_nula(3, 3)
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    """

    lista = []
    lista_final = []

    for _ in range(n):
        lista.append(0)

    for _ in range(m):
        lista_final.append(lista)

    return lista_final


def eh_regular(a: list[list[int]]) -> bool:
    regular = True
    i = 1
    while i < len(a) and regular:
        if len(a[0]) != len(a[i]):
            regular = False
    i = i + 1
    return regular


def conta_zeros(a: list[list[int]]) -> int:
    """
    Conta a quantidade de zeros da matriz *a*.
    Exemplos
    >>> conta_zeros([[1, 0, 7], [0, 1, 0]])
    3
    >>> conta_zeros([[1, 0], [1, 2], [0, 2]])
    2
    """

    contagem = 0

    for i in a:
        for j in i:
            if j == 0:
                contagem = contagem + 1

    return contagem


def transposta(a: list[list[int]]) -> list[list[int]]:
    """
    Cria a matriz transposta de *a*.
    Requer que *a* seja regular.
    Exemplos
    >>> transposta([[4, 5, 1], [7, 8, 9]])
    [[4, 7], [5, 8], [1, 9]]
    >>> transposta([[4, 1], [7, 8], [2, 6], [5, 3]])
    [[4, 7, 2, 5], [1, 8, 6, 3]]
    """
    t = []
    for j in range(len(a[0])):
        coluna = []
        for i in range(len(a)):
            coluna.append(a[i][j])
        t.append(coluna)
    return t
