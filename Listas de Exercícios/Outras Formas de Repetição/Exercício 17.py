def soma(lista: list[int], valor: int) -> int:
    """
    Determina quantos elementos de *lista* precisam ser somados para atingir
    *valor*

    Exemplos
    >>> soma([1, 2, 4], 7)
    3
    >>> soma([1, 2, 4], 3)
    2
    >>> soma([1, 2, 4], 4)
    -1
    """

    soma: int = 0
    contador: int = 0
    resposta = -1
    i: int = 0

    while resposta == -1 and i < len(lista):
        soma = soma + lista[i]
        contador = contador + 1
        if soma == valor:
            resposta = contador
        i = i + 1

    return resposta
