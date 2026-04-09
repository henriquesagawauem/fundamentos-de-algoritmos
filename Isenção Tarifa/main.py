# Análise
# Definir se uma pessoa é isenta de tarifa, onde os isentos são apenas
# quem tem menos de 18 anos ou mais de 65 anos, caso contrário o sistema
# não deve retornar que não é isento de tarifa
#
# Tipos de dados
# A idade do usuário

def isento_tarifa(idade: int) -> bool:
    """
    Produz True se uma pessoa de *idade* anos é isento da tarifa
    de transporte público, isto é, tem menos que 18 anos ou 65
    ou mais. Produz False caso contrário.
    Exemplos
    >>> isento_tarifa(17)
    True
    >>> isento_tarifa(18)
    True
    >>> isento_tarifa(50)
    False
    >>> isento_tarifa(65)
    True
    >>> isento_tarifa(70)
    True
    """
    return idade <= 18 or idade >= 65
