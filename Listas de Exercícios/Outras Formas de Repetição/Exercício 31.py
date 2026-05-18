def itens(n: int) -> int:
    """
    >>> itens(1)
    1
    >>> itens(10)
    512
    """
    return 2 ** (n - 1)


def itens2(n: int) -> int:
    """
    >>> itens2(1)
    1
    >>> itens2(0)
    512
    """
    item: int = 1

    for _ in range(n - 1):
        item = item * 2

    return item
