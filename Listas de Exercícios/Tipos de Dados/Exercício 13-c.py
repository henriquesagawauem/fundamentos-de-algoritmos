from enum import Enum, auto


class Direcao(Enum):
    NORTE = auto()
    SUL = auto()
    LESTE = auto()
    OESTE = auto()


# Análise
# retornar a direção correspondente a 90° da direção informada em sentido horário
#
# Tipos de dados
# as direção norte, sul, leste e oeste e retorna alguma direção norte, sul, leste e oeste


def direcao_90graus(direcao: Direcao) -> Direcao:
    """
    retorna a direção correspondente a 90° de *direcao* no sentido horário

    Exemplos
    >>> direcao_90graus(Direcao.NORTE).name
    'LESTE'
    >>> direcao_90graus(Direcao.LESTE).name
    'SUL'
    >>> direcao_90graus(Direcao.SUL).name
    'OESTE'
    >>> direcao_90graus(Direcao.OESTE).name
    'NORTE'
    """

    if direcao == Direcao.NORTE:
        return Direcao.LESTE
    elif direcao == Direcao.LESTE:
        return Direcao.SUL
    elif direcao == Direcao.SUL:
        return Direcao.OESTE
    elif direcao == Direcao.OESTE:
        return Direcao.NORTE


def direcao_90graus_anti(direcao: Direcao) -> Direcao:
    """
    retorna a direção correspondente a 90° de *direcao* no sentido anti-horário

    Exemplos
    >>> direcao_90graus_anti(Direcao.NORTE).name
    'OESTE'
    >>> direcao_90graus_anti(Direcao.LESTE).name
    'NORTE'
    >>> direcao_90graus_anti(Direcao.SUL).name
    'LESTE'
    >>> direcao_90graus_anti(Direcao.OESTE).name
    'SUL'
    """

    return direcao_90graus(direcao_90graus(direcao_90graus(direcao)))
