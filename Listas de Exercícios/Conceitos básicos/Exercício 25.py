# 25) Dizemos que o nome de uma pessoa é curto se tem no máximo três letras e longo se tem mais que 8
# letras. Um nome que não é nem curto e nem longo é mediano. Projete uma função que verifique se
# um dado nome é mediano.

# -----------------------------------------------------------------------------------------------------------------------

# Análise
# Verifica se o nome de uma pessoa é mediano usando os padrões de 
# um nome pequeno tem no máximo 3 letras e um longo mais de 8 letras

# tipos de dados
# nome de um pessoa

def nome_mediano(nome: str) -> bool:
    """
    Compara o *nome* para verificar se é mediano, onde um nome pequeno tem no máximo 
    3 letras e um longo mais de 8 letras, ou seja, deve ter entre 3 e 8 letras

    Exemplos
    >>> nome_mediano("bu")
    False
    >>> nome_mediano("felipe")
    True
    >>> nome_mediano("Alexandre")
    False
    """

    return 3 < len(nome) <= 8