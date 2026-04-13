# 12) Faça uma função chamada aumenta que recebe dois números positivos, um valor e uma porcentagem,
# e calcula o resultado de aumentar a porcentagem ao valor. Confira na janela de interações se a função
# funciona de acordo com os exemplos a seguir
# >>> aumenta(100.0, 3.0)
# 103.0
# >>> aumenta(20.0, 50.0)
# 30.0
# >>> aumenta(10.0, 80.0)
# 18.0

# -------------------------------------------------------------------

# Análise
# Calcular a soma de um número com a sua respectiva porcentagem
#
# Tipos de dados
# Dois números positivos, sendo eles um valor e uma porcentagem

def aumenta(valor: float, porcentagem: float) -> float:
    """
    Calcular a soma de *valor* com *porcetagem* cujo a variável *porcentagem* representa
    a parcentagem do valor

    Exemplos
    >>> aumenta(100.0, 3.0)
    103.0
    >>> aumenta(20.0, 50.0)
    30.0
    >>> aumenta(10.0, 80.0)
    18.0
    """

    return valor + ((valor * porcentagem) / 100)