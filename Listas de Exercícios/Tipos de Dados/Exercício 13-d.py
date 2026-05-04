from enum import Enum, auto


class Direcao(Enum):
    NORTE = auto()
    SUL = auto()
    LESTE = auto()
    OESTE = auto()


def direcao_inversa(direcao: Direcao) -> Direcao:
    """
    Retorna a direção oposta a *direcao*

    Exemplos
    >>> direcao_inversa(Direcao.NORTE).name
    'SUL'
    >>> direcao_inversa(Direcao.SUL).name
    'NORTE'
    >>> direcao_inversa(Direcao.OESTE).name
    'LESTE'
    >>> direcao_inversa(Direcao.LESTE).name
    'OESTE'
    """

    if direcao == Direcao.NORTE:
        return Direcao.SUL
    elif direcao == Direcao.SUL:
        return Direcao.NORTE
    elif direcao == Direcao.OESTE:
        return Direcao.LESTE
    else:
        return Direcao.OESTE


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


def girar(direcao1: Direcao, direcao2: Direcao) -> int:
    """
    Retorna a quantidade de graus que uma pessoa precisa girar em sentido
    horário para sair de *direcao'* e olhar para *direcao2*

    >>> girar(Direcao.NORTE, Direcao.LESTE)
    90
    >>> girar(Direcao.NORTE, Direcao.SUL)
    180
    >>> girar(Direcao.NORTE, Direcao.OESTE)
    270
    >>> girar(Direcao.LESTE, Direcao.NORTE)
    270
    """

    if direcao_inversa(direcao1) == direcao2:
        return 180
    elif direcao_90graus(direcao1) == direcao2:
        return 90
    elif direcao1 == direcao2:
        return 0
    else:
        return 270
