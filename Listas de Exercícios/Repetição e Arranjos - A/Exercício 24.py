from enum import Enum, auto


class Voto(Enum):
    PRIMEIRO = auto()
    SEGUNDO = auto()
    BRANCO = auto()


def eleicao(votos: list[Voto]) -> Voto:
    """
    Calcula o resultado das eleições

    Exemplos
    >>> eleicao([Voto.PRIMEIRO, Voto.PRIMEIRO, Voto.SEGUNDO, Voto.BRANCO]).name
    'PRIMEIRO'
    >>> eleicao([Voto.PRIMEIRO, Voto.BRANCO, Voto.BRANCO, Voto.BRANCO]).name
    'BRANCO'
    >>> eleicao([Voto.PRIMEIRO, Voto.PRIMEIRO, Voto.SEGUNDO, Voto.SEGUNDO]).name
    'BRANCO'
    """
    primeiro: int = 0
    segundo: int = 0
    branco: int = 0

    for voto in votos:
        if voto == Voto.PRIMEIRO:
            primeiro = primeiro + 1
        elif voto == Voto.SEGUNDO:
            segundo = segundo + 1
        elif voto == Voto.BRANCO:
            branco = branco + 1

    resultado: Voto = Voto.PRIMEIRO

    if segundo > primeiro:
        resultado = Voto.SEGUNDO
    elif branco > segundo and branco > primeiro or primeiro == segundo:
        resultado = Voto.BRANCO

    return resultado
