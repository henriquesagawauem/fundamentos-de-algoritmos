from dataclasses import dataclass
from enum import Enum, auto


class Ordem(Enum):
    CRESCENTE = auto()
    DECRESCENTE = auto()
    NENHUM = auto()


@dataclass
class Sequencia:
    a: int
    b: int
    c: int


def verificar_ordem(sequencia: Sequencia) -> Ordem:
    """
    Verifica se uma sequencia de três números é crescente, decrescente ou nenhum

    Exemplos
    >>> verificar_ordem(Sequencia(1, 2, 3)).name
    'CRESCENTE'
    >>> verificar_ordem(Sequencia(3, 2, 1)).name
    'DECRESCENTE'
    >>> verificar_ordem(Sequencia(2, 3, 1)).name
    'NENHUM'
    """
    if (
        sequencia.a > sequencia.b
        and sequencia.b > sequencia.c
        and sequencia.c < sequencia.a
    ):
        return Ordem.DECRESCENTE
    elif (
        sequencia.c > sequencia.b
        and sequencia.b > sequencia.a
        and sequencia.a < sequencia.c
    ):
        return Ordem.CRESCENTE
    return Ordem.NENHUM
