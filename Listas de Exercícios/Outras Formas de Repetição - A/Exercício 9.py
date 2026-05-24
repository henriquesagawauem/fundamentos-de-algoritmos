
def repeticao(l: list[int]) -> bool:
    """
    Verifica se uma lista tem dois elementos consecutivos iguais

    Exemplos
    >>> repeticao([1, 2, 2, 1])
    True
    >>> repeticao([1, 2, 3, 4])
    False
    >>> repeticao([1, 2, 3, 4, 4])
    True
    """
    for i in range(1, len(l)):
        if l[i - 1] == l[i]:
            return True

    return False