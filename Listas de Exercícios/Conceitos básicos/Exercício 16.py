# 16) Faça uma função chamada censura que recebe dois argumentos, uma string frase e um número
# natural n, e produz uma nova frase trocando as primeiras n letras da frase de entrada por n 'x'.
# Confira na janela de interações se a função funciona de acordo com os exemplos a seguir
# >>> censura('droga de lanche!', 5)
# 'xxxxx de lanche!'
# >>> censura('ferrou geral!', 6)
# 'xxxxxx geral!'

# ---------------------------------------------------------------------------------------------------------

# Análise
# Censurar as n primeiras letras de uma frase, trocando elas por 'x'.
#
# Tipos de dados
# Uma frase do usuário e um número inteiro positivo

def censura(frase: str, n: int) -> str:
    """
    Censurar *frase* trocando as *n* primeiras letras
    por *n* 'x'

    Exemplos
    >>> censura('droga de lanche!', 5)
    'xxxxx de lanche!'
    >>> censura('ferrou geral!', 6)
    'xxxxxx geral!'
    """

    return "x" * n + frase[n:]