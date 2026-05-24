def maior(lista: list[int]) -> int:
    """
    Retorna a maior sequencias de dias consecutivos que os preços subiram

    Exemplos
    >>> maior([1, 2, 3, 1, 1, 1, 2])
    2
    >>> maior([1, 2, 3, 4])
    3
    """
    dias: int = 0
    maior_seq: int = 0

    for i in range(1, len(lista)):
        if lista[i] > lista[i - 1]:
            dias = dias + 1

            if dias > maior_seq:
                maior_seq = dias
        else:
            dias = 0

    return maior_seq