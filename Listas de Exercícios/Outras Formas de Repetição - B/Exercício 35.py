def poltronas(m: list[list[int]], n: int) -> bool:
    """
    Verifica se existe uma fileira com pelo menos n poltronas
    livres consecutivas para acomodar um grupo de amigos.

    Exemplos
    >>> poltronas([[0, 0, 1, 0], [0, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]], 7)
    True
    >>> poltronas([[0, 0, 1, 0], [0, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]], 8)
    False
    >>> poltronas([[0, 0, 1, 0], [0, 1, 1, 1], [0, 0, 0, 0]], 4)
    True
    """
    existe = False
    for i in range(len(m)):
        contador = 0
        eh_sequencia = True
        j = 0
        while j < len(m[i]) and eh_sequencia:
            if m[i][j] == 0 and not contador == n:
                contador = contador + 1
            else:
                eh_sequencia = False
            j = j + 1
        if contador == n:
            existe = True
    return existe
