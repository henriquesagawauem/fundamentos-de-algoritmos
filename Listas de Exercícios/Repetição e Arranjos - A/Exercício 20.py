from dataclasses import dataclass
from enum import Enum, auto


@dataclass
class Coordenadas:
    x: int
    y: int
    z: int


class Direcoes(Enum):
    NORTE = auto()
    SUL = auto()
    LESTE = auto()
    OESTE = auto()
    CIMA = auto()
    BAIXO = auto()


def calcula(coordenada: Coordenadas, lista: list[Direcoes]) -> Coordenadas:
    """
    Calcula a posição final de um personagem nas coordenadas X, Y, Z, tal que, *lista*
    contém a sequência de movimentos

    Exemplos
    >>> calcula(
    ...     Coordenadas(0, 0, 0),
    ...     [
    ...         Direcoes.NORTE,
    ...         Direcoes.NORTE,
    ...         Direcoes.LESTE,
    ...         Direcoes.CIMA,
    ...         Direcoes.CIMA,
    ...     ],
    ... )
    Coordenadas(x=2, y=2, z=1)
    """

    for i in lista:
        if i == Direcoes.NORTE:
            coordenada.x = coordenada.x + 1
        elif i == Direcoes.SUL:
            coordenada.x = coordenada.x - 1
        elif i == Direcoes.LESTE:
            coordenada.z = coordenada.z + 1
        elif i == Direcoes.OESTE:
            coordenada.z = coordenada.z - 1
        elif i == Direcoes.CIMA:
            coordenada.y = coordenada.y + 1
        elif i == Direcoes.BAIXO:
            coordenada.y = coordenada.y - 1

    return coordenada
