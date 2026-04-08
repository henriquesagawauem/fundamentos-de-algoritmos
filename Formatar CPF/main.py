def format_cpf(cpf: str) -> str:
    """
    Formata o cpf de um usuário para ser representado com a formatação padrão
    xxx.xxx.xxx-xx. Portanto, recebe o cpf sem formatação (12345678910) e retorna
    formado padrão (123.456.789-10)

    Exemplos
    >>> format_cpf('12345678912')
    '123.456.789-12'
    """
    return f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"