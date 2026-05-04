from enum import Enum, auto


class Direcao(Enum):
    NORTE = auto()
    SUL = auto()
    LESTE = auto()
    OESTE = auto()


# Análise
# Projetar uma função que recebe uma direção e retorna a direção inversa a ela
#
# Tipos de dados
# Direções norte, sul, leste e oeste


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
