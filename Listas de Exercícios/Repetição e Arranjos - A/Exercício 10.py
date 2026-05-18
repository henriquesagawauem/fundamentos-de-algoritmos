def concatenar(lista: list[str]) -> str:
    """
    Concatena todos os elementos de *lista*

    Exemplos
    >>> concatenar(['palmeiras', '123'])
    'palmeiras123'
    """
    string: str = ''
    for i in lista:
        string = string + i

    return string
