def procura(lista: list[str], alvo: str) -> bool:
    """
    Exemplos
    >>> procura(['palmeiras', 'nada', 'santos'], 'palmeiras')
    True
    >>> procura(['palmeiras', 'nada', 'santos'], 'tudo')
    False
    >>> procura(['palmeiras', 'nada', 'santos'], 'santos')
    True
    """
    encontrou = False
    if len(lista) > 0:
        if lista[0] == alvo:
            encontrou = True
        else:
            encontrou = procura(lista[1:], alvo)
    return encontrou
