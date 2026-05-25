from enum import Enum, auto


class Resposta(Enum):
    SIM = auto()
    NAO = auto()


def calc_radical(alturas: list[float]) -> Resposta:
    """
    >>> calc_radical([10.0, 10.0, 20.0, 20.0, 20.0]).name
    'SIM'
    >>> calc_radical([10.0, 10.0, 10.0, 20.0, 20.0]).name
    'NAO'
    """
    # calcula a média
    soma = 0
    for altura in alturas:
        soma = soma + altura

    media = soma / len(alturas)

    # Verifica se tem mais de 3 alturas maiores que a média

    contador = 0
    for altura in alturas:
        if altura > media:
            contador = contador + 1

    eh_radical = Resposta.NAO

    if contador >= 3:
        eh_radical = Resposta.SIM

    return eh_radical
