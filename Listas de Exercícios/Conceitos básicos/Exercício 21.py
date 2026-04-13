# 21) Faça uma função chamada termina_z que recebe uma string s e indica se s termina com a letra 'z'.
# Confira na janela de interações se a função funciona de acordo com os exemplos a seguir
# >>> termina_z('arroz')
# True
# >>> termina_z('')
# False
# >>> termina_z('Z')
# True
# >>> termina_z('casa')
# False

# ---------------------------------------------------------------------------------------------------------

# Análise
# Verifica se um string termina em Z
#
# Tipos de dados
# um string

def termina_z(string: str) -> bool:
    """
    Retorna True caso o último caractere de *string* seja igual 'z'. Obs: 'z' podeser tanto maiúsculo quanto minúsculo

    Exemplos
    >>> termina_z('arroz')
    True
    >>> termina_z('')
    False
    >>> termina_z('Z')
    True
    >>> termina_z('casa')
    False
    """

    return string != "" and string.lower()[len(string) - 1] == "z"