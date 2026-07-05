def remove_vazio(lista: list[str]) -> None:
    """
    Remove todos os elementos vázios de uma lista

    Exemplos
    >>> lst = ['a', 'b', '', 'c']
    >>> remove_vazio(lst)
    >>> lst
    ['a', 'b', 'c']


    >>> lst = ['a', '', '', 'c']
    >>> remove_vazio(lst)
    >>> lst
    ['a', 'c']
    """
    i = 0

    while i < len(lista):
        if lista[i] == "":
            for j in range(i, len(lista) - 1):
                lista[j] = lista[j + 1]
            
            
            lista.pop()
            i -= 1
        i += 1