# Henrique Tutomu Sagawa 152725

from enum import Enum, auto
from dataclasses import dataclass

# Questão 1

# Análise
# Calcular o desempenho de um determinado time de futebol, baseado em seu
# histórico de partidas.
#
# Tipos de dados
# O registro de uma partida de futebol, com nome do time 1 (string) e nome do time 2 (string), a quantidade de gols feito
# pelo time 1 (int) e a quantidade de gols feito pelo time 2 (int), também recebe o nome do time (string) que quer análisar e retorna o desempenho
# do time escolhido com seu número de pontos (int), número de vitórias (int) e saldo de gols (int).


@dataclass
class Partida:
    """Representa uma partida de futebol."""

    time1: str
    time2: str
    gols1: int
    gols2: int


@dataclass
class Desempenho:
    """Representa o desempenho acumulado de um time."""

    pontos: int
    vitorias: int
    saldo_gols: int


def calc_desempenho(partidas: list[Partida], nome: str) -> Desempenho:
    """
    Calcula o desempenho do time *nome*, baseado no histórico de partida, em *partidas*,
    análisando seu número de pontos, número de vitórias e saldo de gols. Obs: uma vitórias
    vale 3 pontos, empate 1 ponto, derrata 0 pontos e o saldo de gols é dado pela diferenças
    de gols feito pelo *nome* e os gols feitos pelo adversário.

    Exemplos
    >>> calc_desempenho(
    ...     [
    ...         Partida('Time A', 'Time B', 5, 1),
    ...         Partida('Time C', 'Time A', 2, 0),
    ...         Partida('Time A', 'Time D', 1, 1),
    ...     ],
    ...     'Time A',
    ... )
    Desempenho(pontos=4, vitorias=1, saldo_gols=2)
    >>> calc_desempenho(
    ...     [
    ...         Partida('Time A', 'Time B', 5, 1),
    ...         Partida('Time C', 'Time A', 2, 0),
    ...         Partida('Time A', 'Time D', 1, 1),
    ...     ],
    ...     'Time C',
    ... )
    Desempenho(pontos=3, vitorias=1, saldo_gols=2)
    >>> calc_desempenho(
    ...     [
    ...         Partida('Time A', 'Time B', 5, 1),
    ...         Partida('Time C', 'Time A', 2, 0),
    ...         Partida('Time A', 'Time D', 1, 1),
    ...     ],
    ...     'Time D',
    ... )
    Desempenho(pontos=1, vitorias=0, saldo_gols=0)
    >>> calc_desempenho(
    ...     [
    ...         Partida('Time A', 'Time B', 5, 1),
    ...         Partida('Time C', 'Time A', 2, 0),
    ...         Partida('Time A', 'Time D', 1, 1),
    ...     ],
    ...     'Time B',
    ... )
    Desempenho(pontos=0, vitorias=0, saldo_gols=-4)
    """

    pontos: int = 0
    vitorias: int = 0
    saldo: int = 0

    for i in partidas:
        if i.time1 == nome:
            saldo = saldo + (i.gols1 - i.gols2)
            if i.gols1 > i.gols2:
                pontos = pontos + 3
                vitorias = vitorias + 1
            elif i.gols1 == i.gols2:
                pontos = pontos + 1
        elif i.time2 == nome:
            saldo = saldo + (i.gols2 - i.gols1)
            if i.gols2 > i.gols1:
                pontos = pontos + 3
                vitorias = vitorias + 1
            elif i.gols2 == i.gols1:
                pontos = pontos + 1

    return Desempenho(pontos, vitorias, saldo)


# ==========================================================================================

# Questão 2

# Análise
# Verifica se a mesada paga pelo é o suficiente para cobrir as despesas de Matheus
# em um determinado mês, onde o pai vai cobrir em cada um dos gastos do mês o valor
# equivalente ao menor gasto identificado.
#
# Tipos de dados
# Recebe os gastos de Matheus em uma lista de floats, e recebe a valor da mesada de
# seu pai (float), e retorna um valor booleano indicando se a mesada é suficiente ou não
# True para suficiente e False para não suficiente


def verifica_mesada(gastos: list[float], mesada: float) -> bool:
    """
    Verifica se *mesada* é suficiente para cobrir a diferenças dos valores de
    *gastos* com o menor valor de *gastos*

    Exemplos
    >>> verifica_mesada([40, 60, 20, 50, 20, 100], 300)
    True
    >>> verifica_mesada([100, 180, 120, 220, 190, 120, 150], 250)
    False
    >>> verifica_mesada([500, 350, 200, 600, 820], 740)
    False
    >>> verifica_mesada([200], 10)
    True
    """
    # Verifica o menor valor de todos
    menor: float = gastos[0]
    for i in range(1, len(gastos)):
        if gastos[i] < menor:
            menor = gastos[i]

    # Calcular a diferença com o menor gasto
    for i in range(len(gastos)):
        gastos[i] = gastos[i] - menor

    # Calcula a soma das diferenças
    soma: float = 0
    for i in gastos:
        soma = soma + i

    # Verifica se a mesa é suficiente
    eh_suficiente = False
    if mesada >= soma:
        eh_suficiente = True

    return eh_suficiente

