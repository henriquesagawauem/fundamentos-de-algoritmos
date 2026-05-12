def maior(l: list[int]) -> int:
    """
    Retorna o índice no maior elemento de *l*

    Exemplos
    >>> maior([5, 4, 3])
    0
    >>> maior([1, 2, 3])
    2
    >>> maior([1, 4, 3])
    1
    """
    maior = l[0]
    maior_in = 0

    for i in range(len(l)):
        if maior <= l[i]:
            maior_in = i
            maior = l[i]

    return maior_in


def ordem(l: list[int]) -> bool:
    """
    Verifica se *l* está em ordem não decrescente

    Exemplos
    >>> ordem([1, 2, 3])
    True
    >>> ordem([1, 2, 3, 1])
    False
    >>> ordem([1, 2, 3, 1, 2])
    False
    >>> ordem([1, 2, 3, 5, 9])
    True
    """
    temp = 0

    for i in range(len(l)):
        if l[i] < temp:
            return False
        temp = l[i]

    return True


def lista_par(l: list[int]) -> list[int]:
    """
    Retorna uma lista com os elementos em índices pares de *l*

    Exemplos
    >>> lista_par([1, 2, 3, 4, 5, 6, 7, 8])
    [1, 3, 5, 7]
    """

    nova = []

    for i in range(len(l)):
        if i % 2 == 0:
            nova.append(l[i])

    return nova


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
