from enum import Enum, auto


class Tipo(Enum):
    """Classificação do nome de uma pessoa com base no número de caracteres"""

    LONGO = auto()
    CURTO = auto()
    MEDIANO = auto()


def verificar_nome(nome: str) -> Tipo:
    """
    Verifica o nome de uma pessoa é curto se tem no máximo quatro
    letras e longo se tem mais que 8 letras. Um nome que não é nem
    curto e nem longo é mediano.

    Exemplos
    >>> verificar_nome('Abel').name
    'CURTO'
    >>> verificar_nome('Vitor Roque').name
    'LONGO'
    >>> verificar_nome('Flaco').name
    'MEDIANO'
    """

    if len(nome) <= 4:
        return Tipo.CURTO
    elif len(nome) > 8:
        return Tipo.LONGO

    return Tipo.MEDIANO
