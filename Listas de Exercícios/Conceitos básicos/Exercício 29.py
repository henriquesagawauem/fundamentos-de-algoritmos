# 29) Projete uma função que verifique se o último nome (sobrenome) de uma pessoa é “Silva”. Você pode
# assumir que a string de entrada não tem espaços no início e no final e que contém pelo menos um
# espaço em branco.

# -------------------------------------------------------------------------------------------------------------------

# Análise
# Verifica se o último nome (sobrenome) de uma pessoa é "Silva
#
# Tipos de dados
# nome da pessoa

def sobrenome_eh_silva(nome: str) -> bool:
    """
    Verifica se o último nome (sobrenome) de *nome* é "Silva". Assumindo que a string de entrada não tem 
    espaços no início e no final e que contém pelo menos um espaço em branco.

    Exemplos
    >>> sobrenome_eh_silva("João Silva")
    True
    >>> sobrenome_eh_silva("Silva João")
    False
    """
    return nome.split()[len(nome.split()) - 1].lower() == "silva"