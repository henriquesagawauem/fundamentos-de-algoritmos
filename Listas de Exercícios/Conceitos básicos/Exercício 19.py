# 19) Faça uma função chamada par que recebe um número natural n e indica se n é par. Um número é par
# se o resto da divisão dele por 2 é igual a zero. Confira na janela de interações se a função funciona de
# acordo com os exemplos a seguir
# >>> par(3)
# False
# >>> par(6)
# True

# ------------------------------------------------------------------------------------------------------------------

# Análise
# Indica se um número natural é par, retornado True ou False
#
# Tipos de dados
# Um número inteiro positivo

def par(n: int) -> bool:
    """
    Retorna True se *n* for um número par, isso pode ser feito verificando
    se o resto da divisão de *n* for igual a zero.

    Exemplos
    >>> par(3)
    False
    >>> par(6)
    True
    """

    return n % 2 == 0