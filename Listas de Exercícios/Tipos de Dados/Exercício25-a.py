from dataclasses import dataclass


@dataclass
class Ponto:
    """
    Coordenadas horizontal e vertical de um tela, representadas por números inteiros
    """

    x: int
    y: int


@dataclass
class Janela:
    """
    Coordenadas de uma janela de uma tela
    """

    x_min: int
    x_max: int
    y_min: int
    y_max: int


def vali(janela: Janela, clique: Ponto) -> bool:
    """
    Verifica se um clique aconteceu dentro de uma janela

    Exemplos
    >>> vali(Janela(1, 4, 1, 5), Ponto(2, 3))
    True
    >>> vali(Janela(1, 4, 1, 5), Ponto(2, 0))
    False
    """
    x_valido = janela.x_min <= clique.x and clique.x <= janela.x_max
    y_valido = janela.y_min <= clique.y and clique.y <= janela.y_max

    return x_valido and y_valido