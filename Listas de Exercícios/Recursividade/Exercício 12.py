def procura(lista: list[int]) -> bool:
    """
    Verifica se *lista* é uma lista de binários

    Exemplos
    >>> procura([1, 0, 0, 0, 1, 1])
    True
    >>> procura([1, 1, 0, 0, 2])
    False
    """
    resposta = True

    if len(lista) > 0:
        if lista[0] == 1 or lista[0] == 0:
            resposta = procura(lista[1:])
        else:
            resposta = False
    return resposta
