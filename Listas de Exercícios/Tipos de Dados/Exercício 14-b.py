from enum import Enum, auto


class Elevador(Enum):
    """A situação atual do elevador"""

    SUBINDO = auto()
    DESCENDO = auto()
    PARADO = auto()


def situacao_elevador(atual: int, solicitado: int) -> Elevador:
    """
    Deve retornar qual será o situação do elevador dependendo do andar no qual
    ele estiver, baseado em *solicitado* e o andar atual

    Exemplos
    >>> situacao_elevador(3, 1).name
    'DESCENDO'
    >>> situacao_elevador(1, 4).name
    'SUBINDO'
    >>> situacao_elevador(1, 1).name
    'PARADO'
    """

    if atual > solicitado:
        return Elevador.DESCENDO
    elif atual == solicitado:
        return Elevador.PARADO
    else:
        return Elevador.SUBINDO


def pode_movimentar(atual: Elevador) -> bool:
    """
    Verifica se um elevador pode se movimentar, visto que ele só pode se movimentar
    caso a situação atual dele seja PARADO.

    Exemplos
    >>> pode_movimentar(Elevador.PARADO)
    True
    >>> pode_movimentar(Elevador.SUBINDO)
    False
    >>> pode_movimentar(Elevador.DESCENDO)
    False
    """

    if atual == Elevador.PARADO:
        return True

    return False
