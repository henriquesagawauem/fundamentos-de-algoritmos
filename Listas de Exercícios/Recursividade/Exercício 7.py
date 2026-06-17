def produto(n: int) -> int:
    """
    Calcula o produto dos números 1, 2, ..., *n*

    Exemplo
    >>> produto(5)
    120
    """

    resultado = 1

    if n > 0:
        resultado = n * produto(n - 1)
    
    return resultado