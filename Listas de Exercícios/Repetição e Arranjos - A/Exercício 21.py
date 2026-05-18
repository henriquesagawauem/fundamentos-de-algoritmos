def calc_doacao(saldo: float, movimentacao: list[float]) -> int:
    """
    Calcula quanto deve ser doado toda vez que a conta ficar negativa

    Exemplos
    >>> calc_doacao(50, [-60.0, -20.0, 40.0, -15.0])
    20
    """

    total_doacao: int = 0
    esta_negativo: bool = saldo < 0

    for i in movimentacao:
        saldo = saldo + i

        if saldo < 0:
            if not esta_negativo:
                total_doacao = total_doacao + 10
                esta_negativo = True
        else:
            esta_negativo = False

    return total_doacao
