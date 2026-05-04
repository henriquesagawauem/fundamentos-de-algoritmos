from dataclasses import dataclass
from enum import Enum, auto


@dataclass
class Desempenho:
    """
    Desempenho de cada time de futebol no campeonato, em número de pontos e vitórias e saldo de gols.
    """

    pontos: int
    vitorias: int
    saldo: int


class Time(Enum):
    """Times de futebol em critério de desempate"""

    TIME1 = auto()
    TIME2 = auto()


def melhor_desempenho(time1: Desempenho, time2: Desempenho) -> Time:
    """
    Verifica qual time teve o melhor desempenho no campeonato

    Exemplos
    >>> melhor_desempenho(Desempenho(12, 4, 15), Desempenho(11, 3, 17)).name
    'TIME1'
    >>> melhor_desempenho(Desempenho(12, 4, 15), Desempenho(12, 4, 17)).name
    'TIME2'
    >>> melhor_desempenho(Desempenho(12, 5, 15), Desempenho(12, 4, 17)).name
    'TIME1'
    """

    if time1.pontos > time2.pontos:
        return Time.TIME1

    if time1.vitorias > time2.vitorias:
        return Time.TIME1

    if time1.saldo > time2.saldo:
        return Time.TIME1

    return Time.TIME2


class Resultado(Enum):
    """Possíveis resultados de uma partida de futebol"""

    VITORIA = auto()
    EMPATE = auto()
    DERROTA = auto()


def atualizar(atual: int, resultado: Resultado) -> int:
    """
    Adiciona a quantidade certa de pontos de cada time baseada no resultado de uma partida do time de futebol

    Exemplos
    >>> atualizar(15, Resultado.VITORIA)
    18
    >>> atualizar(15, Resultado.EMPATE)
    16
    >>> atualizar(15, Resultado.DERROTA)
    15
    """

    if resultado == Resultado.VITORIA:
        return atual + 3
    elif resultado == Resultado.EMPATE:
        return atual + 1
    else:
        return atual
