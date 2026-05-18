from dataclasses import dataclass


@dataclass
class Desempenho:
    pontos: int
    vitorias: int
    saldo: int


@dataclass
class Partida:
    time: int
    adversario: int


def calc_desempenho(partidas: list[Partida]) -> Desempenho:
    """
    Calcule o desempenho de um time de futebol

    Exemplos
    >>> calc_desempenho([Partida(3, 1), Partida(1, 3), Partida(1, 1)])
    Desempenho(pontos=4, vitorias=1, saldo=0)
    """
    pontos: int = 0
    vitorias: int = 0
    saldo: int = 0
    for i in partidas:
        if i.time > i.adversario:
            pontos = pontos + 3
            vitorias = vitorias + 1
        elif i.time == i.adversario:
            pontos = pontos + 1

        saldo = saldo + (i.time - i.adversario)

    return Desempenho(pontos, vitorias, saldo)
