def maior_sequencia_zeros(lista: list[int]) -> int:
    """
    Encontra a maior sequencia de zeros
    
    Exemplos
    >>> maior_sequencia_zeros([0, 0, 2, 1, 0, 0, 0, 7, 0, 0, 0, 0, 0])
    5
    """
    return aux(lista, 0, 0)


def aux(lista: list[int], atual: int, maior: int) -> int:
    resultado = []

    if lista == []:
        resultado = encontra_maior(atual, maior)
    else:
        if lista[0] == 0:
            resultado = aux(lista[1:], atual + 1, maior)
        else:
            resultado = aux(lista[1:], 0, encontra_maior(atual, maior))

    return resultado


def encontra_maior(num1: int, num2: int) -> int:
    """
    Encontra o maior valor entre dois nums
    
    Exemplos
    >>> encontra_maior(2, 0)
    2
    >>> encontra_maior(1, 3)
    3
    """
    resultado = 0
    if num1 >= num2:
        resultado = num1
    else:
        resultado = num2

    return resultado