# 28) Projete uma função que determine se três medidas podem formar um triângulo.

# -------------------------------------------------------------------------------------------------------------------

# Análise
# Verifica se três medidas podem formar um triângulo
#
# Tipos de dados
# medidas dos lados do triângulo

def pode_formar_triangulo(a: float, b: float, c: float) -> bool:
    """
    Verifica se as medidas *a*, *b* e *c* podem formar um triângulo. Para isso, é necessário que a soma de 
    quaisquer dois lados seja maior que o terceiro lado.

    Exemplos
    >>> pode_formar_triangulo(3, 4, 5)
    True
    >>> pode_formar_triangulo(1, 2, 3)
    False
    """
    return (a + b > c) and (a + c > b) and (b + c > a)