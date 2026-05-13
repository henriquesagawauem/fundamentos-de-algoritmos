def cria_matriz_nula(m: int, n: int) -> list[list[int]]:
    """
    Cria uma matriz nula com *m* linhas e *n* colunas.
    Requer que m > 0 e n > 0.
    Exemplos
    >>> cria_matriz_nula(2, 3)
    [[0, 0, 0], [0, 0, 0]]

    >>> cria_matriz_nula(3, 3)
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    """

    lista = []
    lista_final = []

    i = 0
    j = 0

    while i < n:
        lista.append(0)
        i = i + 1

    while j < m:
        lista_final.append(lista)
        j = j + 1

    return lista_final


def eh_regular(a: list[list[int]]) -> bool:
    """Produz True se *a* é uma matriz
    regular, isto é, todas as linhas tem a
    mesma quantidade de elementos.
    Exemplos
    >>> eh_regular([])
    True
    >>> eh_regular([[2]])
    True
    >>> eh_regular([[2], [4]])
    True
    >>> eh_regular([[2], [4, 1]])
    False
    >>> eh_regular([[2, 1, 6], [4, 0, 1]])
    True
    >>> eh_regular([[2, 1], [4, 0, 1]])
    False
    >>> eh_regular([[2], [4], [7]])
    True
    """

    for i in a:
        if len(i) != len(a[0]):
            return False
    return True


def conta_zeros(a: list[list[int]]) -> int:
    """
    Conta a quantidade de zeros da matriz *a*.
    Exemplos
    >>> conta_zeros([[1, 0, 7], [0, 1, 0]])
    3
    >>> conta_zeros([[1, 0], [1, 2], [0, 2]])
    2
    """

    contagem = 0

    for i in a:
        for j in i:
            if j == 0:
                contagem = contagem + 1

    return contagem


def fatorial(n: int) -> int:
    """
    Calcula o produto de todos os naturais
    entre 1 e n, isto é, 1 * ... * (n - 1) * n.
    Exemplos
    >>> fatorial(0)
    1
    >>> fatorial(1)
    1
    >>> fatorial(2)
    2
    >>> fatorial(3)
    6
    >>> fatorial(4)
    24
    """

    produto = 1

    for i in range(1, n + 1):
        produto = produto * i
    return produto


def palindromo(lst: list[int]) -> bool:
    """Produz True se *lst* é palíndromo, isto
    é, tem os mesmos elementos quando vistos
    da direita para a esquerda e da esquerda
    para a direita. Produz False caso contrário.
    >>> palindromo([])
    True
    >>> palindromo([4])
    True
    >>> palindromo([1, 1])
    True
    >>> palindromo([1, 2])
    False
    >>> palindromo([1, 2, 1])
    True
    >>> palindromo([1, 5, 5, 1])
    True
    >>> palindromo([1, 5, 1, 5])
    False
    """

    nova_lista = []

    for i in range(1, len(lst) + 1):
        nova_lista.append(lst[len(lst) - i])

    for j in range(len(nova_lista)):
        if lst[j] != nova_lista[j]:
            return False
    return True


def primo(n: int) -> bool:
    """
    Produz True se *n* é um número primo,
    isto é, tem exatamente dois divisores
    distintos, 1 e ele mesmo. Produz False
    se *n* não é primo.
    Exemplos
    >>> primo(1)  # 1
    False
    >>> primo(2)  # 1 2
    True
    >>> primo(3)  # 1 3
    True
    >>> primo(5)  # 1 5
    True
    >>> primo(8)  # 1 2 4 8
    False
    >>> primo(11)  # 1 11
    True
    """

    contador = 0

    for i in range(n):
        if n % (i + 1) == 0:
            contador = contador + 1

    return contador == 2
