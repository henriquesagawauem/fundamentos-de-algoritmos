# 13) Faça uma função chamada zera_dezena_e_unidade que recebe um número natural n e devolve um
# novo número que é como n mas tem o valor da dezena e unidade zero. Dica: use piso da divisão.
# Confira na janela de interações se a função funciona de acordo com os exemplos a seguir

# >>> zera_dezena_e_unidade(19)
# 0
# >>> zera_dezena_e_unidade(341)
# 300
# >>> zera_dezena_e_unidade(5251)
# 5200

# ------------------------------------------------

# Análise
# Receber um número inteiro e retorná-lo com sua dezena e unidade zerados
#
# Tipos de dados
# Um número inteiro e positivo

def zera_dezena_e_unidade(n: int) -> int:
    """
    Retornar o número *n", mas com o valor da dezena e unidade zerados

    Exemplos
    >>> zera_dezena_e_unidade(19)
    0
    >>> zera_dezena_e_unidade(341)
    300
    >>> zera_dezena_e_unidade(5251)
    5200
    """

    return (n // 100) * 100