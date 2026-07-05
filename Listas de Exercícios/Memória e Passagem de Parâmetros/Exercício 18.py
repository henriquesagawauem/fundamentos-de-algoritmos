def ordenacao_selecao(lista: list[int]) -> None:
    """
    Ordena uma lista de inteiros em ordem crescente usando o método de ordenação por seleção.

    Exemplos
    >>> lista = [3, 1, 4, 2]
    >>> ordenacao_selecao(lista)
    >>> lista
    [1, 2, 3, 4]
    """

    for i in range(len(lista)):
        menor_indice = i

        for j in range(i, len(lista)):
            if lista[j] < lista[menor_indice]:
                menor_indice = j
        
        if menor_indice != i:
            temp = lista[i]
            lista[i] = lista[menor_indice]
            lista[menor_indice] = temp