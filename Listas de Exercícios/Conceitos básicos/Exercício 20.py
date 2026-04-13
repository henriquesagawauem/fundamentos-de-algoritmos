# 20) Faça uma função chamada tres_digitos que recebe um número natural n e verifica se n tem exata-
# mente 3 dígitos. Confira na janela de interações se a função funciona de acordo com os exemplos a

# seguir
# >>> tres_digitos(99)
# False
# >>> tres_digitos(100)
# True
# >>> tres_digitos(999)
# True
# >>> tres_digitos(1000)
# False

# -------------------------------------------------------------------------------------------------------------

# Análise
# Verifica se um número possui exatamente 3 dígitos
#
# Tipos de dados
# Um número inteiro e positivo

def tres_digitos(n: int) -> bool:
    """
    Conta o número de caracteres de *n* e caso seja igual a
    3 retorna True, caso contrário, retorna False

    Exemplos
    >>> tres_digitos(99)
    False
    >>> tres_digitos(100)
    True
    >>> tres_digitos(999)
    True
    >>> tres_digitos(1000)
    False
    """

    return len(str(n)) == 3