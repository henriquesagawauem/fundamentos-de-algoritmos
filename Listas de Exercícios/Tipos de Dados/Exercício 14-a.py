from enum import Enum, auto


class Elevador(Enum):
    """A situação atual do elevador"""

    SUBINDO = auto()
    DESCENDO = auto()


def situacao_elevador(atual: int, solicitado: int) -> Elevador:
    """
    Deve retornar qual será o situação do elevador dependendo do andar no qual
    ele estiver, baseado em *solicitado* e o andar atual

    Exemplos
    >>> situacao_elevador(3, 1).name
    'DESCENDO'
    >>> situacao_elevador(1, 4).name
    'SUBINDO'
    >>> situacao_elevador(2, 1).name
    'DESCENDO'
    """

    assert atual != solicitado, 'Os andares devem ser diferentes'

    if atual > solicitado:
        return Elevador.DESCENDO
    else:
        return Elevador.SUBINDO
