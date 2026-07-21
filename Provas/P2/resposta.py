# Henrique Tutomu Sagawa - 152725

# ========================================================================================

# Exercício 1

# Análise
# Uma função recursiva que conta quantos elementos de uma lista de strings possuem
# um determinado número de caracteres.

# Tipos de dados
# Uma lista contendo elementos no formato string, o valor do número de caracteres (int) e
# o indice de início (int), geralmente 0. A função retorna um valor inteiro (int) contendo o
# número de strings com o número determinado de caracteres


def conta_strings(lista: list[str], n: int, indice: int) -> int:
    """
    Conta quantos elementos, de forma recursiva, em *lista* possuem a quantidade
    *n* de caracteres, iniciando a busca pelo início da lista, incrementando a partir de
    *indice*.

    Exemplos
    >>> conta_strings(['palmeiras', 'flamengo', 'santos', 'times'], 5, 0)
    1
    >>> conta_strings(['palmeiras', 'flamengo1', 'santos', 'times'], 10, 0)
    0
    >>> conta_strings(['123', '1', '123', '2342', '239284', '123'], 3, 0)
    3
    >>> conta_strings([], 0, 0)
    0
    >>> conta_strings([], 1, 0)
    0
    >>> conta_strings(['', '123', ''], 0, 0)
    2
    >>> conta_strings(['oi'], 2, 0)
    1
     >>> conta_strings(
    ...     [
    ...         'brasil',
    ...         'noruega',
    ...         'croacia',
    ...         'belgica',
    ...         'alemanha',
    ...         'holanda',
    ...         'franca',
    ...     ],
    ...     7, 0
    ... )
    4

    """

    contador: int = 0

    if indice <= len(lista) - 1:
        if len(lista[indice]) == n:
            contador += 1

        contador = contador + conta_strings(lista, n, indice + 1)

    return contador


# ================================================================================================

# Exercício 2

# Análise
# Recebe duas listas, e a função deve trocar os elementos entre as duas listas a partir
# de um índice específico, sem utilizar listas auxiliares nem o operador de sublista.

# Tipos de dados
# Duas listas de inteiros (int), podendo ter tamanhos variados, e um índice (int), e deve alterar
# os valores de cada uma das listas.


def trocar_elementos(lista1: list[int], lista2: list[int], indice: int) -> None:
    """
    Troca elemenetos entre *lista1* e *lista2* a partir de o índice *indice*
    sem usar listas auxiliares e sem usar operadores de sublistas.

    Exemplos
    >>> lst1 = [1, 2, 3, 4, 5, 6]
    >>> lst2 = [9, 7, 8, 0]
    >>> trocar_elementos(lst1, lst2, 2)
    >>> lst1
    [1, 2, 8, 0, 5, 6]
    >>> lst2
    [9, 7, 3, 4]

    >>> lst1 = [1, 2, 3, 4, 5]
    >>> lst2 = [1, 2, 3, 5]
    >>> trocar_elementos(lst1, lst2, 3)
    >>> lst1
    [1, 2, 3, 5, 5]
    >>> lst2
    [1, 2, 3, 4]

    >>> lst1 = [1, 2, 3]
    >>> lst2 = [4, 3, 2, 1]
    >>> trocar_elementos(lst1, lst2, 1)
    >>> lst1
    [1, 3, 2]
    >>> lst2
    [4, 2, 3, 1]

    >>> lst1 = [1, 2, 3, 4]
    >>> lst2 = [4, 3, 2, 1]
    >>> trocar_elementos(lst1, lst2, 0)
    >>> lst1
    [4, 3, 2, 1]
    >>> lst2
    [1, 2, 3, 4]

    >>> lst1 = [1, 2, 3, 4]
    >>> lst2 = [4, 3, 2, 1]
    >>> trocar_elementos(lst1, lst2, 4)
    >>> lst1
    [1, 2, 3, 4]
    >>> lst2
    [4, 3, 2, 1]

    >>> lst1 = []
    >>> lst2 = []
    >>> trocar_elementos(lst1, lst2, 1)
    >>> lst1
    []
    >>> lst2
    []

    >>> lst1 = [1, 2, 3]
    >>> lst2 = [4, 3, 2, 1]
    >>> trocar_elementos(lst1, lst2, 3)
    >>> lst1
    [1, 2, 3]
    >>> lst2
    [4, 3, 2, 1]
    """

    # encontra a lista com a menor quantidade de elementos
    menor: int = 0
    if len(lista1) <= len(lista2):
        menor = len(lista1)
    else:
        menor = len(lista2)

    for i in range(menor):
        if i >= indice:
            temp = lista1[i]
            lista1[i] = lista2[i]
            lista2[i] = temp


# =======================================================================================
# Exercício 3

# Análise
# A função deve contar o número de inversões em um arranjo, isto é, uma inversão ocorre quando um par
# de elementos está fora de ordem, ou seja, dado um arranjo qualquer A, uma inversão é qualquer par de
# índices (i, j) tal que i < j, mas A[i] > A[j].
#
# Tipos de dados
# Recebe uma lista contendo números inteiros (int) e retorna um valor inteiro (int) que contém a
# quantidade de inversões na lista.


def contar_inversoes(lista: list[int]) -> int:
    """
    Conta o número de inversões em *lista*, isto é, quando em qualquer par de índices (i, j)
    tal que i < j mas o elemento de *lista* no índice i é maior que o elemento de índice j

    Exemplos
    >>> contar_inversoes([4, 3, 5, 1])
    4
    >>> contar_inversoes([1, 2, 3, 4, 5, 6, 7])
    0
    >>> contar_inversoes([1, 3, 5, 1, 6, 2])
    5
    >>> contar_inversoes([1])
    0
    >>> contar_inversoes([1, 2])
    0
    >>> contar_inversoes([2, 1])
    1
    >>> contar_inversoes([1, 1])
    0
    >>> contar_inversoes([])
    0
    """

    contador: int = 0

    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if i < j and lista[i] > lista[j]:
                contador += 1

    return contador