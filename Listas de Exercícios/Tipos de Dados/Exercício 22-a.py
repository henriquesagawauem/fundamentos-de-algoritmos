from enum import Enum, auto
from dataclasses import dataclass

# Análise
# Verificar qual dos times obteve o maior desempenha, baseado em critérios de desempate como número de pontos
# número de vitórias e saldo de gols.

# Tipos de dados
# Os dados referentes a dois times em números de golsm vitórias e saldo de gols, representados por inteiros positivos. e retorna qual time ganhou

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
