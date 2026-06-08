def split(string: str) -> list[str]:
    """
    Recebe uma palavra, e remove os espaços em brancos
    dividindo cada parte em uma lista

    Exemplos
    >>> split('Cristiano Ronaldo')
    ['Cristiano', 'Ronaldo']
    >>> split('Neymar Junior')
    ['Neymar', 'Junior']
    """
    lista_palavras = []
    palavra = ''

    for i in range(len(string)):
        if string[i] != ' ':
            palavra = palavra + string[i]

        else:
            lista_palavras.append(palavra)

            palavra = ''

    lista_palavras.append(palavra)

    return lista_palavras


def nome_usuario(nome: str) -> str:
    """
    Cria um nome de usuário a partir de *nome*
    da seguinte forma:
    - divide *nome* em partes (separadas por
    espaço)
    - junta a primeira letra de cada parte
    (exceto a última) e a última parte toda
    O resultado é truncado para 8 caractes
    em minúsculo.
    >>> nome_usuario('Maria')
    'maria'
    >>> nome_usuario('Pedro Paulo')
    'ppaulo'
    >>> nome_usuario('José Paulo da Silveira')
    'jpdsilve'
    """

    partes = split(nome)
    usuario = ''

    for i in range(len(partes) - 1):
        usuario = usuario + partes[i][0]
    if len(partes) > 0:
        usuario = usuario + partes[len(partes) - 1]
    return usuario[:8].lower()
