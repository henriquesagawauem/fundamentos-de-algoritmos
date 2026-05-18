def calc_laurea(notas: list[float]) -> bool:
    """
    Verifica se um aluno pode receber a Laurea Academica

    Exemplos
    >>> calc_laurea([6.7, 8.9, 6.5, 9.9])
    False
    >>> calc_laurea([9.1, 9.9, 9.7, 9.0, 10])
    True
    """

    contador: int = 0

    for nota in notas:
        if nota > 9.0:
            contador = contador + 1

    return contador > len(notas) * (2 / 3)
