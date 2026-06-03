def soma(lst: list[int], n: int) -> None:
    """
    Exemplos
    >>> lst = [1, 2, 3, 4, 5]
    >>> soma(lst, 1)
    >>> lst
    [2, 3, 4, 5, 6]
    """
    for i in range(len(lst)):
        lst[i] = lst[i] + n
