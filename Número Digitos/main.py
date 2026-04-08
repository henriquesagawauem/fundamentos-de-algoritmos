def numero_digitos(n: int) -> int:
    """
    Retorna o número de caracteres contidos em *n*. Para números negativas,
    deverá converter para o valor absoluto da variável

    Exemplos
    >>> numero_digitos(-345)
    3
    >>> numero_digitos(345)
    3
    """
    return len(str(abs(n)))