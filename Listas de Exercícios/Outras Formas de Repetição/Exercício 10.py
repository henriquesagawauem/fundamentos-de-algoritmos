def ocorrencias(l: list[str], nome: str) -> list[int]:
    """
    Encontra as posições das ocorrências de *nome* em *l*

    Exemplos
    >>> ocorrencias(['teste', 'fernando', 'teste'], 'teste')
    [0, 2]
    """

    r = []

    for i in range(len(l)):
        if l[i] == nome:
            r.append(i)

    return r