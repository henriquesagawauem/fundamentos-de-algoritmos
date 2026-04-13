# 10) Faça uma função chamada area_retangulo que recebe dois argumentos, a largura e a altura de um
# retângulo, e calcula a sua área. Confira na janela de interações se a função funciona de acordo com os
# exemplos a seguir
# >>> area_retangulo(3.0, 5.0)
# 15.0
# >>> area_retangulo(2.0, 2.5)
# 5.0

# ----------------------------------------------------------------------------------------

# Análise
# Calcular a área de um retângulo
#
# Tipos de dados
# Medidas dos dois lados de um retângulo (lado 1 e lado 2), ambos na mesma unidade de medidda
# que não é definida, mas para ambos os lados devem ser a mesma


def area_retangulo(l1: float, l2: float) -> float:
    """
    Calcular a área de um ratângulo utilizando as medidas de *l1* e *l2*
    multiplicando-os (l1 * l2). Obs: ambos os lados devem utilizar a mesma
    unidade de medida

    Exemplos
    >>> area_retangulo(3.0, 5.0)
    15.0
    >>> area_retangulo(2.0, 2.5)
    5.0
    """
    return l1 * l2