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

