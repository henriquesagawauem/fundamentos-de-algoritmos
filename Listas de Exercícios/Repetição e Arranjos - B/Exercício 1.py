from dataclasses import dataclass


@dataclass
class Aluno:
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


def media_geral(l: list[Aluno]) -> float:
    """
    Calcula a média geral dos alunos de *l*

    Exemplos
    >>> media_geral(
    ...     [
    ...         Aluno('Alfredo', 6.0, 74.0),
    ...         Aluno('Bianca', 5.9, 75.0),
    ...         Aluno('Jorge', 6.0, 75.0),
    ...         Aluno('Leonidas', 5.9, 74.0),
    ...         Aluno('Maria', 8.0, 90.0),
    ...     ]
    ... )
    6.359999999999999
    """

    soma: float = 0

    for i in l:
        soma = soma + i.media

    return soma / len(l)


def media_freq(l: list[Aluno]) -> float:
    """
    Calcula a média dos alunos de *l* com frequência acima de 75%

    Exemplos
    >>> media_freq(
    ...     [
    ...         Aluno('Alfredo', 6.0, 74.0),
    ...         Aluno('Bianca', 5.9, 75.0),
    ...         Aluno('Jorge', 6.0, 75.0),
    ...         Aluno('Leonidas', 5.9, 74.0),
    ...         Aluno('Maria', 8.0, 90.0),
    ...     ]
    ... )
    6.633333333333333
    """

    soma: float = 0
    count: int = 0

    for i in l:
        if i.frequencia >= 75.0:
            soma = soma + i.media
            count = count + 1

    return soma / count


def acima_med(l: list[Aluno]) -> list[str]:
    """
    devolve uma lista com o nome de todos os alunos frequentes em *l*,
    que possuem médias acima da média geral dos frequentes.

    Exemplos
    >>> acima_med(
    ...     [
    ...         Aluno('Alfredo', 6.0, 74.0),
    ...         Aluno('Bianca', 5.9, 75.0),
    ...         Aluno('Jorge', 6.0, 75.0),
    ...         Aluno('Leonidas', 5.9, 74.0),
    ...         Aluno('Maria', 8.0, 90.0),
    ...     ]
    ... )
    ['Maria']
    """

    nomes: list[str] = []

    for i in l:
        if i.frequencia >= 75 and i.media >= media_freq(l):
            nomes.append(i.nome)
    return nomes


def media_sup(l: list[Aluno]) -> list[Aluno]:
    """
    devolve uma lista com todos os dados dos alunos com média
    superior a 8,5 em *l*.

    Exemplos
    >>> media_sup(
    ...     [
    ...         Aluno('Alfredo', 6.0, 74.0),
    ...         Aluno('Bianca', 5.9, 75.0),
    ...         Aluno('Jorge', 6.0, 75.0),
    ...         Aluno('Leonidas', 5.9, 74.0),
    ...         Aluno('Maria', 8.6, 90.0),
    ...     ]
    ... )
    [Aluno(nome='Maria', media=8.6, frequencia=90.0)]
    """

    alunos: list[Aluno] = []

    for i in l:
        if i.media >= 8.5:
            alunos.append(i)

    return alunos
