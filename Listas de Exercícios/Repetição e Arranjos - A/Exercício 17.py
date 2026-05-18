from enum import Enum, auto


class Sinal(Enum):
    POSITIVO = auto()
    NEGATIVO = auto()


def compara(lista: list[int]) -> Sinal:
    """
    Verifica se *lista* tem mais valores positivos do que negativos

    Exemplos
    >>> compara([1, 2, 3, -1, -2, -3, -4]).name
    'NEGATIVO'
    >>> compara([1, 2, 3, 4, 5, -1, -2, -3, -4]).name
    'POSITIVO'
    """

    count_pos: int = 0
    count_neg: int = 0

    maior: Sinal = Sinal.POSITIVO

    for i in lista:
        if i < 0:
            count_neg = count_neg + 1
        else:
            count_pos = count_pos + 1

    if count_neg > count_pos:
        maior = Sinal.NEGATIVO

    return maior
