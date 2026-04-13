# 18) Faça uma função chamada vogal que recebe um caractere c e verifica se c é uma vogal minúscula (a,
# e, i, o, u). Confira na janela de interações se a função funciona de acordo com os exemplos a seguir
# >>> vogal('a')
# True
# >>> vogal('b')
# False
# >>> vogal('e')
# True
# >>> vogal('A')
# False

# -------------------------------------------------------------------------------------------------------------

# Análise
# Verifica se uma letra é uma vogal
#
# Tipos de dados
# uma vogal minúscula

def vogal(c: str) -> bool:
    """
    Retornar True se *c* for uma vogal minúscula (a, e, i, o, u)

    Exemplos
    >>> vogal('a')
    True
    >>> vogal('b')
    False
    >>> vogal('e')
    True
    >>> vogal('A')
    False
    """

    return c == "a" or c == "e" or c == "i" or c == "o" or c == "u" 