def str_int(string: str) -> list[int]:
    """
    Recebe uma string no formato ('xx, xx, xx') e retorna uma lista de inteiros

    Exemplos
    >>> str_int('512,12,145')
    [512, 12, 145]
    """
    lista_cod: list[int] = []
    texto_atual: str = ''

    for caractere in string:
        if caractere == ',':
            if texto_atual != '':
                lista_cod.append(int(texto_atual))
                texto_atual = ''
        else:
            texto_atual = texto_atual + caractere

    if texto_atual != '':
        lista_cod.append(int(texto_atual))

    return lista_cod
