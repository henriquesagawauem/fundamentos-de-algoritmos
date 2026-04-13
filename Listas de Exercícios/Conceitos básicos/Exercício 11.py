# 11) Faça uma função chamada produto_anterior_posterior que recebe um número inteiro n e calcula
# o produto de n, n + 1 e n - 1.

# ------------------------------------------------------

# Análise
# Calcular o produto de um número inteiro n, n + 1 e n - 1
#
# Tipos de dados
# Número inteiro n

def produto_anterior_posterior(n: int) -> int:
    """
    Calcular o produto de um número inteiro n, n + 1 e n - 1

    Exemplos
    >>> produto_anterior_posterior(3)
    24
    >>> produto_anterior_posterior(5)
    120
    """
    return n * (n + 1) * (n - 1)