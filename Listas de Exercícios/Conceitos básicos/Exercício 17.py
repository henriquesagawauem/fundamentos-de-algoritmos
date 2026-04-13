# 17) Faça uma função chamada no_intervalo que recebe um número inteiro n, um limite inferior ini e um
# limite superior fim, e verifica se n está no intervalo fechado [ini, fim]. Confira na janela de interações
# se a função funciona de acordo com os exemplos a seguir
# >>> no_intervalo(5, 1, 10)
# True
# >>> no_intervalo(1, 1, 10)
# True
# >>> no_intervalo(0, 1, 10)
# False
# >>> no_intervalo(11, 1, 10)
# False

# -----------------------------------------------------------------------------------------------------------

# Análise
# Verificar se o número x está entre o intervalo determinado pelo usuário
#
# Tipos de dados
# três números reais (ini, x, fim)

def no_intervalo(x: float, ini: float, fim: float) -> bool:
    """
    Retornar True se o valor *x* estiver entre o intervalor de [ini, fim], caso contrário
    retorna False

    Exemplos
    >>> no_intervalo(5, 1, 10)
    True
    >>> no_intervalo(1, 1, 10)
    True
    >>> no_intervalo(0, 1, 10)
    False
    >>> no_intervalo(11, 1, 10)
    False
    """

    return ini <= x <= fim