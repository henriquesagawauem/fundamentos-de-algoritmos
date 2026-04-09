# Análise
# Receber um CPF sem formatação e formtá-lo para o padrão xxx.xxx.xxx-xx
#
# Tipos de dados
# CPF do usuário, onde o CPF não tem formtação


def formatar_cpf(cpf: str) -> str:
    """
    Receber o cpf do usuário sem formatação, no formato de string
    e retorná-lo formatado no padrão xxx.xxx.xxx-xx

    Exemplos
    >>> formatar_cpf("12345678901")
    '123.456.789-01'
    >>> formatar_cpf("98765432110")
    '987.654.321-10'
    """
    return f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"


# Análise
# Receber um cpf com formatação xxx.xxx.xxx-xx e remover sua formatação para xxxxxxxxxxx
#
# Tipos de dados
# CPF do usuário, onde o CPF está formatado em xxx.xxx.xxx-xx


def desformatar_cpf(cpf: str) -> str:
    """
    Recebero cpf do usuário com formatação, no formato de string
    e retorná-lo sem formatação

    Exemplos
    >>> desformatar_cpf("123.456.789-01")
    '12345678901'
    """
    return f"{cpf[0:3]}{cpf[4:7]}{cpf[8:11]}{cpf[12:14]}"
