def melhor_volta(lista: list[float]) -> int:
    """
    Calcula a melhor melhora de um piloto em voltas de uma corrida

    Exemplos
    >>> melhor_volta([60.0, 58.5, 59.0, 55.0])
    4
    """
    maior_melhora: float = lista[0] - lista[1]
    volta: int = 2

    for i in range(1, len(lista)):
        tempo_anterior: float = lista[i - 1]
        tempo_atual: float = lista[i]

        melhora_atual: float = tempo_anterior - tempo_atual

        if melhora_atual > maior_melhora:
            maior_melhora = melhora_atual
            volta = i + 1

    return volta
