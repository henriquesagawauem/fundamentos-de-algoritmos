from enum import Enum, auto


class Jogada(Enum):
    PEDRA = auto()
    PAPEL = auto()
    TESOURA = auto()


class Vencedor(Enum):
    JOGADOR1 = auto()
    JOGADOR2 = auto()
    EMPATE = auto()


def jogo(jogador1: Jogada, jogador2: Jogada) -> Vencedor:
    """
    Verificar quem ganhou uma partida de pedra papel e tesoura

    Exemplos
    >>> jogo(Jogada.TESOURA, Jogada.PEDRA).name
    'JOGADOR2'
    >>> jogo(Jogada.TESOURA, Jogada.PAPEL).name
    'JOGADOR1'
    """

    if jogador1 == jogador2:
        return Vencedor.EMPATE
    elif (
        (jogador1 == Jogada.PAPEL and jogador2 == Jogada.TESOURA)
        or (jogador1 == Jogada.TESOURA and jogador2 == Jogada.PEDRA)
        or (jogador1 == Jogada.PEDRA and jogador2 == Jogada.PAPEL)
    ):
        return Vencedor.JOGADOR2

    return Vencedor.JOGADOR1
