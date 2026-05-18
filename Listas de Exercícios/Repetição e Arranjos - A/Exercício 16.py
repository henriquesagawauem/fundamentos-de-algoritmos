def ordenar(lista: list[int]) -> list[int]:
    """
    Ordena uma lista de número inteiros
    """
    if len(lista) <= 1:
        return lista

    pivo: int = lista[0]
    menores: list[int] = []
    maiores: list[int] = []

    for i in range(1, len(lista)):
        if lista[i] <= pivo:
            menores.append(lista[i])
        else:
            maiores.append(lista[i])

    return menores + [pivo] + maiores


def amplitude(lista: list[int]) -> int:
    """
    Calcula a amplitude entre o maior e o menor valor de *lista*

    Exemplo
    >>> amplitude([1, 3, 2, 1, 4])
    3
    """

    lista_ordenada = ordenar(lista)

    return lista_ordenada[len(lista) - 1] - lista_ordenada[0]
