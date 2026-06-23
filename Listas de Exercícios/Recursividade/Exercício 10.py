def concatenar(lista: list[str]) -> str:
    """
    Exemplos
    >>> concatenar(['palmeiras', '123'])
    'palmeiras123'
    """
    resultado = ''
    if len(lista) > 0:
        resultado = lista[0] + concatenar(lista[1:])
    return resultado
