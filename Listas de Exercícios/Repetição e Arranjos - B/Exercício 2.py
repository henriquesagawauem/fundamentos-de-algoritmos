from dataclasses import dataclass


@dataclass
class Capitulo:
    titulo: str
    pagina: int


def sumario(l: list[Capitulo]) -> list[str]:
    """
    receba uma lista com os títulos dos capítulos e as páginas de início de cada
    capítulo (um número) e devolva uma lista (de strings) com as linhas do sumário no formato acima,
    sabendo que cada linha possui espaço para 30 caracteres e que o título do capítulo sempre tem no
    máximo 25 caracteres. Garante que o título do capítulo fique em letras maiúsculas na linha final e que a
    página possua sempre dois caracteres.

    Exemplos
    >>> sumario([Capitulo('Rio Negro', 12), Capitulo('Solimões', 9)])
    ['Rio Negro...................12', 'Solimões....................09']
    """

    sumario: list[str] = []

    for i in l:
        string: str = ''
        string = string + i.titulo[:25]
        for _ in range(30 - (len(i.titulo) + 2)):
            string = string + '.'
        if i.pagina < 10:
            string = string + '0' + str(i.pagina)
        else:
            string = string + str(i.pagina)

        sumario.append(string)

    return sumario
