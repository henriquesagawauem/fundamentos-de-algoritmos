from enum import Enum, auto


class Bandeira(Enum):
    VERDE = auto()
    AMARELA = auto()
    VERMELHA_PATAMAR_1 = auto()
    VERMELHA_PATAMAR_2 = auto()


def calc_tarifa(consumo: float, bandeira: Bandeira, tarifa: float) -> float:
    """
    Determina o valor final que o consumidor tem que pagar dado o seu consumo em
    quilowatt-hora, a tarifa básica do quilowatt-hora e a bandeira tarifária.

    Exemplos
    >>> calc_tarifa(100, Bandeira.VERDE, 0.50)
    50.0
    """

    if bandeira == Bandeira.VERDE:
        acrescimo_por_kwh = 0.0
    elif bandeira == Bandeira.AMARELA:
        acrescimo_por_kwh = 0.01874
    elif bandeira == Bandeira.VERMELHA_PATAMAR_1:
        acrescimo_por_kwh = 0.03971
    elif bandeira == Bandeira.VERMELHA_PATAMAR_2:
        acrescimo_por_kwh = 0.09492

    return consumo * (tarifa + acrescimo_por_kwh)
