def menor_num(lista: list[int]) -> int:
    """
    Retorna o menor valor de uma lista de inteiros
    """

    menor: int = lista[0]

    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]

    return menor


def quant_menor(lista: list[int]) -> int:
    """
    Retorna quantas vezes o menor número de *lista* aparece

    Exemplos
    >>> quant_menor([1, 2, 3, 4, 0, 23, 0])
    2
    """

    menor: int = menor_num(lista)
    cont: int = 0

    for i in lista:
        if i == menor:
            cont = cont + 1

    return cont
