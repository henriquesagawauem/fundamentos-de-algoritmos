def quicksort(lista: list[float]) -> list[float]:
    """
    Ordena uma lista do menor para o maior

    Exemplos
    >>> quicksort([1, -1, 32])
    [-1, 1, 32]
    """
    if len(lista) <= 1:
        return lista
    else:
        pivo: float = lista[0]

        menores = []
        maiores = []

        for i in lista[1:]:
            if i <= pivo:
                menores.append(i)
            else:
                maiores.append(i)

        return quicksort(menores) + [pivo] + quicksort(maiores)


def maior_num(l: list[float]) -> float:
    """
    Retorna o maior número em *l*

    Exemplos
    >>> maior_num([32, 12, -1])
    32
    >>> maior_num([1, 32, 2])
    32
    >>> maior_num([3, 1, -2, 45, 34, 65, 100, 93])
    100
    """
    if l == []:
        return 0
    lista_ordenada: list[float] = quicksort(l)
    return lista_ordenada[len(lista_ordenada) - 1]


# ===================================================================================================


def media_lista(l: list[str]) -> float:
    """
    Retorna a média de caracteres dos elementos de *l*

    Exemplos
    >>> media_lista(['casa'])
    4.0
    >>> media_lista(['casa', 'da'])
    3.0
    >>> media_lista(['casa', 'da', ''])
    2.0
    >>> media_lista(['casa', 'da', '', 'onça'])
    2.5
    """

    soma: float = 0
    for i in l:
        soma = soma + len(i)

    return soma / len(l)


# =====================================================================================================

from dataclasses import dataclass


@dataclass
class Aluno:
    """
    Representa um aluno e o resultado que ele
    obteve em uma disciplina.
    Requer que media esteja entre 0 e 10.
    Requer que frequencia esteja entre 0 e 100.
    """

    nome: str
    media: float
    frequencia: float


def aprovados(l: list[Aluno]) -> list[str]:
    """
    Determina o nome dos *alunos* que foram
    aprovados, isto é, obtiveram
    média >= 6 e frequência >= 75.

    Exemplos
    >>> aprovados(
    ...     [
    ...         Aluno('Alfredo', 6.0, 74.0),
    ...         Aluno('Bianca', 5.9, 75.0),
    ...         Aluno('Jorge', 6.0, 75.0),
    ...         Aluno('Leonidas', 5.9, 74.0),
    ...         Aluno('Maria', 8.0, 90.0),
    ...     ]
    ... )
    ['Jorge', 'Maria']
    """
    aprovados: list[str] = []

    for i in l:
        if i.media >= 6 and i.frequencia >= 75:
            aprovados.append(i.nome)

    return aprovados
