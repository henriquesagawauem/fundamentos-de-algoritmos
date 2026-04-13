# 14) Faça uma função chamada exclamacao que recebe dois argumentos, uma string frase e um número
# natural n, e produz a mesma frase adicionando n pontos de exclamação no final da frase. Confira na
# janela de interações se a função funciona de acordo com os exemplos a seguir
# >>> exclamacao('Nossa', 3)
# 'Nossa!!!'
# >>> exclamacao('Que legal', 1)
# 'Que legal!'
# >>> exclamacao('Nada', 0)
# 'Nada'

# ------------------------------------

# Análise
# retornar a frase do usuário juntamento com um número de "!" também 
# informado pelo usuário

# Tipos de dados
# Uma frase e um número inteiro positivo

def exclamacao(frase: str, n: int) -> str:
    """
    Retornar *frase* juntamento com um número *n* de exclamações

    Exemplos
    >>> exclamacao('Nossa', 3)
    'Nossa!!!'
    >>> exclamacao('Que legal', 1)
    'Que legal!'
    >>> exclamacao('Nada', 0)
    'Nada'
    """

    return frase + "!" * n