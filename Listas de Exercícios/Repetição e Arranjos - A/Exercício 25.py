from dataclasses import dataclass


@dataclass
class Ponto:
    x: float
    y: float


@dataclass
class Retangulo:
    x_min: float
    x_max: float
    y_min: float
    y_max: float


def menor(pontos: list[Ponto]) -> Retangulo:
    """
    Calcula o menor retangulo possível para cobrir os pontos em *pontos*

    Exemplos
    >>> menor(
    ...     [
    ...         Ponto(x=2.0, y=3.0),
    ...         Ponto(x=-1.0, y=5.0),
    ...         Ponto(x=4.0, y=1.0),
    ...         Ponto(x=0.0, y=-2.0),
    ...     ]
    ... )
    Retangulo(x_min=-1.0, x_max=4.0, y_min=-2.0, y_max=5.0)
    """
    x_min = pontos[0].x
    x_max = pontos[0].x
    y_min = pontos[0].y
    y_max = pontos[0].y

    for ponto in pontos:
        if ponto.x < x_min:
            x_min = ponto.x
        elif ponto.x > x_max:
            x_max = ponto.x

        if ponto.y < y_min:
            y_min = ponto.y
        elif ponto.y > y_max:
            y_max = ponto.y

    return Retangulo(x_min, x_max, y_min, y_max)
