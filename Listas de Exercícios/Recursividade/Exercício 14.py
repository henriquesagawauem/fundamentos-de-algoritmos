def tam_max(lista: list[str]) -> int:
    """
    Encontra o tamanho da maior string em uma lista de strings.

    Exemplos
    >>> tam_max(['a', 'ab', 'abc'])
    3
    >>> tam_max(['a', 'ab', 'abc', 'abcd'])
    4
    >>> tam_max([])
    0
    """
    maior: int = 0
    if len(lista) == 1:
        maior = len(lista[0])
    elif len(lista) > 1:
        maior2: int = tam_max(lista[1:])

        if len(lista[0]) > maior2:
            maior = len(lista[0])
        else:
            maior = maior2

    return maior