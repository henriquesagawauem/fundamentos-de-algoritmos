def prefixo(p1: str, p2: str) -> str:
    """
    Verifica o prefixo de *p1* e *p2*

    Exemplos
    >>> prefixo('abacate', 'abacaxi')
    'abaca'
    """

    pref: str = ''

    menor_tamanho = min(len(p1), len(p2))
    for i in range(menor_tamanho):
        if p1[i] == p2[i]:
            pref = pref + p1[i]

    return pref
