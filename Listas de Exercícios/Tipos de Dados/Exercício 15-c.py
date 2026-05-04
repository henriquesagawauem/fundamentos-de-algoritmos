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


def vem_antes(data1: Data, data2: Data) -> bool:
    """
    Verifica se *data1* vem antes de *data2*

    Exemplos
    >>> vem_antes(Data(12, 12, 2023), Data(11, 12, 2023))
    False
    >>> vem_antes(Data(12, 12, 2023), Data(13, 12, 2023))
    True
    >>> vem_antes(Data(12, 11, 2023), Data(13, 12, 2024))
    True
    """

    if data1.ano < data2.ano:
        return True
    elif data1.ano == data2.ano and data1.mes < data2.mes:
        return True
    elif data1.ano == data2.ano and data1.mes == data2.mes and data1.dia < data2.dia:
        return True
    return False
