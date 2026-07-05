def tamanho_string(lista: list[str]) -> list[str]:
    """
    Modifica uma lista de strings deixando todas com o mesmo tamanho. Adiciona 
    espaços em branco ao final das strings se necessário.

    Exemplos
    >>> tamanho_string(['ab', 'abc', 'a'])
    ['ab ', 'abc', 'a  ']
    >>> tamanho_string(['ab', 'abc', 'a', 'abcd'])
    ['ab  ', 'abc ', 'a   ', 'abcd']
    """

    max_length = len(lista[0])
    for i in lista:
        if len(i) > max_length:
            max_length = len(i)
    
    for i in range(len(lista)):
        while len(lista[i]) < max_length:
            lista[i] += " "

    return lista