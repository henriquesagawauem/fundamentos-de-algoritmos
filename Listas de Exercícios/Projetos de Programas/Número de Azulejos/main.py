import math

# Análise
# Definir o número de azulejos ncessários para preencher uma parede com base em altura e comprimero. Cada azulejo é quadrado e tem lado de 0.2 metros. Obs: descartamos recorte de azulejos
#
# Tipos de dados
# Comprimento e largura da parede em metros, e o lado do azulejo em metros. Ambos os valores positivos


def numeroAzulejos(comprimento: float, altura: float) -> int:
    """
    Calcula o número de azulejos de 0,2mx0,2m necessários para azulejar uma
    parede de tamanho *comprimento* x *altura* (em metros) considerando que
    nenhum azulejo é perdido e que recortes são descartados.

    Exemplos
    >>> # math.ceil(1.5 / 0.2) * math.ceil(2.3 / 0.2)
    >>> numeroAzulejos(1.5, 2.3)
    96
    >>> numeroAzulejos(0.2, 0.2)
    1
    >>> numeroAzulejos(0.3, 0.2)
    2
    >>> numeroAzulejos(0.3, 0.3)
    4
    >>> numeroAzulejos(0.4, 0.4)
    4
    """
    return math.ceil(comprimento / 0.2) * math.ceil(altura / 0.2)
