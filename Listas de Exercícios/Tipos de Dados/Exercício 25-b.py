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


def vali_jan(j1: Janela, j2: Janela) -> bool:
    """
    Verifica se duas janelas não se sobrepôem
    
    Exemplos
    
    """
    return not (
        (j1.x_max < j2.x_min)
        or (j1.x_min < j2.x_max)
        or (j1.y_max < j2.y_min)
        or (j1.y_min < j2.y_max)
    )
