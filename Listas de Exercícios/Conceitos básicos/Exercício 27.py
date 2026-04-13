# 27) Projete uma função que verifique se o primeiro nome de uma pessoa é “Paula”. Você pode assumir
# que a string de entrada não tem espaços no início e no final e que contém pelo menos um espaço em
# branco.

# -------------------------------------------------------------------------------------------------------------------

# Análise
# Verifica se o primeiro nome de uma pessoa é "Paula"
#
# Tipos de dados
# nome da pessoa

def nome_eh_paula(nome: str) -> bool:
    """
    Verifica se o primeiro nome de *nome* é "Paula". Assumindo que a string de entrada não tem espaços no 
    início e no final e que contém pelo menos um espaço em branco.

    Exemplos
    >>> nome_eh_paula("Paula Silva")
    True
    >>> nome_eh_paula("João Paula")
    False
    """
    return nome.split()[0].lower() == "paula"