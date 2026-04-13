# 15) Faça uma função chamada primeira_maiuscula que recebe uma string frase e produz a mesma frase
# mas com a primeira letra em maiúscula. Confira na janela de interações se a função funciona de acordo
# com os exemplos a seguir
# >>> primeira_maiuscula('joao venceu.')
# 'Joao venceu.'
# >>> primeira_maiuscula('A Paula é um sucesso.')
# 'A paula é um sucesso.'

# ------------------------------------------------------------------------

# Análise
# Retornar a frase do usuário, mas com a primeira letra em maiúscula e as demais em minúscula
#
# Tipos de dados
# Uma frase

def primeira_maiuscula(frase: str) -> str:
    """
    Retornar *frase* mas com a primeira letra maiúscula e as demais letras minúsculas

    Exemplos
    >>> primeira_maiuscula('joao venceu.')
    'Joao venceu.'
    >>> primeira_maiuscula('A Paula é um sucesso.')
    'A paula é um sucesso.'
    """

    return frase[0].upper() + frase[1:].lower()