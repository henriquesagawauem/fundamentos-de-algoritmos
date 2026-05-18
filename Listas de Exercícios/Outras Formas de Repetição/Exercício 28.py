def email(lista: list[str]) -> str:
    """
    Retorna um email da lista *lista* em português separado por vírgula

    Exemplos
    >>> email(['banana', 'maçã', 'felipe'])
    'banana, maçã e felipe'
    >>> email(['rogerio', 'thomas'])
    'rogerio e thomas'
    >>> email(['rogerio'])
    'rogerio'
    """

    string: str = ''

    if len(lista) == 1:
        string = lista[0]
    else:
        for i in range(len(lista)):
            if i != len(lista) - 1:
                string = string + lista[i] + ', '
            else:
                string = string[: len(string) - 2] + ' e ' + lista[i]

    return string
