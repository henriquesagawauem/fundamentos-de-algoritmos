def eh_impar(n: int) -> int:
    """
    Verifica quantas vezes um número par pode ser dividido
    por 2 até se tornar ímpar

    >>> eh_impar(24)
    3
    """

    temp: float = n
    contador: int = 0

    while temp % 2 == 0:
        temp = temp / 2
        contador = contador + 1

    return contador