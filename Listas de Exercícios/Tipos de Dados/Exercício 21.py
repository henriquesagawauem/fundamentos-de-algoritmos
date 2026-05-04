from enum import Enum, auto
from dataclasses import dataclass


class Direcao(Enum):
    NORTE = auto()
    SUL = auto()
    LESTE = auto()
    OESTE = auto()


@dataclass
class Tabuleiro:
    coluna: int
    linha: int
    direcao: Direcao


def casas(atual: Tabuleiro) -> int:
    """Retorna quantas casas o jogador pode avançar no tabuleiro de xadrez
    Exemplos
    >>> casas(Tabuleiro(4, 5, Direcao.OESTE))
    3
    """
    if atual.direcao == Direcao.NORTE:
        return 10 - atual.linha
    elif atual.direcao == Direcao.LESTE:
        return 10 - atual.coluna
    elif atual.direcao == Direcao.SUL:
        return atual.linha - 1
    elif atual.direcao == Direcao.OESTE:
        return atual.coluna - 1
