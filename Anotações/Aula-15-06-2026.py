def soma_naturais(n: int) -> int:
    """
    Soma todos os número naturais menores
    ou iguais que *n*.
    Requer que n >= 0.
    Exemplos
    >>> soma_naturais(0)
    0
    >>> soma_naturais(1)
    1
    >>> soma_naturais(2)
    3
    >>> soma_naturais(3)
    6
    >>> soma_naturais(4)
    10
    """
    resultado = 0
    if n >= 0:
        resultado = n + soma_naturais(n - 1)
    return resultado


def potencia(a: float, n: int) -> float:
    """
    Calcula *a* elevado a *n*.
    Requer que a != 0 e n >= 0.
    Exemplos
    >>> potencia(2.0, 0)
    1.0
    >>> potencia(2.0, 1)
    2.0
    >>> potencia(2.0, 2)
    4.0
    >>> potencia(2.0, 3)
    8.0
    >>> potencia(3.0, 3)
    27.0
    >>> potencia(3.0, 4)
    81.0
    """

    resultado = 1.0

    if n >= 1:
        resultado = a * potencia(a, n - 1)
    return resultado


def soma(lst: list[int]) -> int:
    """
    Soma os elementos de *lst*.
    Exemplos
    >>> soma([])
    0
    >>> soma([6])
    6
    >>> soma([3, 6])
    9
    >>> soma([7, 3, 6])
    16
    """

    resultado = 0
    if len(lst) >= 1:
        resultado = lst[0] + soma(lst[1:])
    return resultado


def freq(v: int, lst: list[int]) -> int:
    """
    Conta quantas vezes *v* aparece
    em *lst*.
    Exemplos
    >>> freq(1, [])
    0
    >>> freq(1, [7])
    0
    >>> freq(1, [1, 7, 1])
    2
    >>> freq(4, [4, 1, 7, 4, 4])
    3
    """

    resultado = 0

    if len(lst) > 0:
        if lst[0] == v:
            resultado = 1 + freq(v, lst[1:])
        else:
            resultado = freq(v, lst[1:])

    return resultado


def em_ordem(lst: list[int]) -> bool:
    """
    Produz True se os elementos de *lst* estão
    em ordem monotonicamente crescente, False caso
    contrário.
    Exemplos
    >>> em_ordem([])
    True
    >>> em_ordem([3])
    True
    >>> em_ordem([3, 4])
    True
    >>> em_ordem([4, 3])
    False
    >>> em_ordem([3, 3, 5, 6, 6])
    True
    >>> em_ordem([3, 3, 5, 4, 6])
    False
    """

    resultado = False

    if len(lst) >= 2:
        if lst[0] <= lst[1]:
            resultado = True and em_ordem(lst[1:])
    else:
        resultado = True

    return resultado
