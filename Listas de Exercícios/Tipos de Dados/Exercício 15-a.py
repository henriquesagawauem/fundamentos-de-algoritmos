from dataclasses import dataclass


@dataclass
class Data:
    dia: int
    mes: int
    ano: int


def formatar_data(data: str) -> Data:
    """
    Recebe uma data no formato de string e formata para uma estrutura com dia,
    mes e ano

    Exemplos
    >>> formatar_data('15/05/2008')
    Data(dia=15, mes=5, ano=2008)
    """

    dia = int(data[:2])
    mes = int(data[3:5])
    ano = int(data[6:10])

    return Data(dia, mes, ano)
