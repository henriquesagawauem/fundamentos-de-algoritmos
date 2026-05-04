from dataclasses import dataclass


@dataclass
class Tela:
    """
    Altura e largura de uma tela em pixels
    """

    altura: int
    largura: int


def megapixel(tela: Tela) -> float:
    """
    Determina quantos mega pixels tem uma tela/imagem, com base
    em suas dimensões

    Exemplos
    >>> megapixel(Tela(1080, 1920))
    2.0736
    """
    return (tela.altura * tela.largura) / 1000000


from enum import Enum, auto


class Aspecto(Enum):
    PROP_4_3 = auto()
    PROP_16_9 = auto()
    OUTRO = auto()


def resolucao(tela: Tela) -> Aspecto:
    """
    indica se uma resolução tem aspecto (razão entre largura e altura)
    de 4:3, 16:9 ou outro (projete um tipo enumerado para representar o aspecto).

    Exemplos
    >>> resolucao(Tela(1080, 1920)).name
    'PROP_16_9'
    >>> resolucao(Tela(600, 800)).name
    'PROP_4_3'
    """

    if tela.largura * 9 == tela.altura * 16:
        return Aspecto.PROP_16_9

    if tela.largura * 3 == tela.altura * 4:
        return Aspecto.PROP_4_3

    return Aspecto.OUTRO
