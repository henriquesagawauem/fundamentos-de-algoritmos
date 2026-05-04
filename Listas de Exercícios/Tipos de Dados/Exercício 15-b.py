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


def ultimo_dia(data: Data) -> bool:
    """
    Verifica se *data* é o último dia do ano

    Exemplos
    >>> ultimo_dia(Data(31, 12, 2023))
    True
    >>> ultimo_dia(Data(12, 9, 2023))
    False
    """

    if data.dia == 31 and data.mes == 12:
        return True

    return False
