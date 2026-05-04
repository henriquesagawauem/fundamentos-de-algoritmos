from dataclasses import dataclass
from enum import Enum, auto


@dataclass
class Reserva:
    inicio: int
    fim: int


def verificar(reserva1: Reserva, reserva2: Reserva) -> bool:
    """
    Verifica se duas reservar no hotel não tem conflito

    Exemplos
    >>> verificar(Reserva(9, 12), Reserva(13, 15))
    True
    >>> verificar(Reserva(9, 12), Reserva(11, 15))
    False
    """
    return not ((reserva1.inicio < reserva2.fim) and (reserva2.inicio < reserva1.fim))
