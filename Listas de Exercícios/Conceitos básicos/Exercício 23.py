# 23) Projete uma função que calcule o valor da hipotenusa a partir dos valores dos catetos.

# ------------------------------------------------------------------------------------------------

# Analíse
# Cálcula a hipotenusa de um triângulo retângulo a partir de seus catetos
#
# Tipos de dados
# cateto oposto e cateto adjacente de um triângulo retângulo, cujo os valores de ambos
# pertence aos número reais

def hipotenusa(cat1: float, cat2: float) -> float:
    """
    Cálcula o valor da hipotenusa de um triângulo retânguo
    utilizando os valores de seus dois catetatos, usando o
    teorema de pitágoras (hip ** 2 = cat1 ** 2 + cat ** 2)

    Exemplos
    >>> hipotenusa(3, 4)
    5
    >>> hipotenusa(6, 8)
    10
    """

    return (cat1 ** 2 + cat2 ** 2) ** 0.5