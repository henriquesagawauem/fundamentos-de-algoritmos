def soma_um(lista: list[int]) -> list[int]:
    """
    Soma 1 a cada elemento da lista.
    Exemplos
    >>> soma_um([1, 2, 3])
    [2, 3, 4]
    """
    resposta = []
    if len(lista) > 0:
        resposta = [lista[0] + 1] + soma_um(lista[1:])

    return resposta