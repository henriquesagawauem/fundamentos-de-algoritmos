def eh_palim(lista: list[int]) -> bool:
    """
    Função que verifica se uma lista é palíndromo.
    Uma lista é palíndromo se ela for igual a ela mesma invertida.
    
    >>> eh_palim([1, 2, 3, 2, 1])
    True
    >>> eh_palim([1, 2, 3, 4, 5])
    False
    >>> eh_palim([1, 2, 3, 4, 1])
    False
    """

    resultado = True

    if len(lista) <= 1:
        resultado = True
    else:
        if lista[0] != lista[len(lista) - 1]:
            resultado = False
        else:
            resultado = eh_palim(lista[1:(len(lista) - 1)])
    
    return resultado