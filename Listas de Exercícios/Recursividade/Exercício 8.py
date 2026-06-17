def gerar(n: int) -> str:
    """
    gera uma string dos números de 1 a *n* separados por virgula

    Exemplos
    >>> gerar(3)
    '1, 2, 3'
    """

    resultado = ''

    if n == 1:
        resultado = '1'
    else:
        resultado = gerar(n - 1) + ", " + str(n)

    return resultado