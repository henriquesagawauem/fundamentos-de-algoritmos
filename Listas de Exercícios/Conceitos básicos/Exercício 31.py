# 31) Projete uma função que encontre o maior valor entre dois números dados.

# --------------------------------------------------------------------------------

# Análise
# Encontrar o maior valor entre dois números dados.
#
# Tipos de dados
# dois números reais

def maior_valor(num1: float, num2: float) -> float:
    """
    Encontra o maior valor entre dois números dados.

    Exemplos
    >>> maior_valor(5.0, 10.0)
    10.0
    >>> maior_valor(15.0, 8.0)
    15.0
    """
    return (num1 + num2 + abs(num1 - num2)) / 2