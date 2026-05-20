# henrique-tutomu-sagawa-152725

from dataclasses import dataclass

# Análise
# Implementar a funcionalidade de buscar todas as informações de livros
# de uma biblioteca com base em um intervalo de anos, ex: livros de 2020 a 2025.
#
# Tipos de dados
# informações do livro, como título (string), sobrenome do primeiro autor (string) e ano de publicaçao (int)
# também a busca, que é o ano mínimo (int) e ano máximo (int), e deve retornar uma lista com dados do
# tipo livro.


@dataclass
class Livro:
    """
    Informações do livro com título (string), sobrenome (string) e ano de publicação (int)

    Requer que o ano seja válido
    """

    titulo: str
    sobrenome: str
    ano: int


@dataclass
class Busca:
    """
    Informações da busca no acervo, com o ano mínimo (int) e ano máximo (int)

    Requer que ano mínimo (ano_min) seja menor que o ano máximo (ano_max)
    """

    ano_min: int
    ano_max: int


def buscar_livros(livros: list[Livro], busca: Busca) -> list[Livro]:
    """
    Faz uma busca de todos os livros, em *livros*, de um determinado intervalo
    de tempo contido em *busca* com o ano mínimo e o ano máximo.

    Exemplos
    >>> buscar_livros(
    ...     [
    ...         Livro('Frio da Madrugada', 'Solimões', 2021),
    ...         Livro('A Gente se Entrega', 'Solimões', 2022),
    ...     ],
    ...     Busca(2020, 2025),
    ... )
    [Livro(titulo='Frio da Madrugada', sobrenome='Solimões', ano=2021), Livro(titulo='A Gente se Entrega', sobrenome='Solimões', ano=2022)]
    >>> buscar_livros(
    ...     [
    ...         Livro('Frio da Madrugada', 'Solimões', 2021),
    ...         Livro('A Gente se Entrega', 'Solimões', 2022),
    ...         Livro('Estrada da Vida', 'Rico', 2019),
    ...     ],
    ...     Busca(2020, 2025),
    ... )
    [Livro(titulo='Frio da Madrugada', sobrenome='Solimões', ano=2021), Livro(titulo='A Gente se Entrega', sobrenome='Solimões', ano=2022)]
    >>> buscar_livros(
    ...     [
    ...         Livro('Frio da Madrugada', 'Solimões', 2021),
    ...         Livro('A Gente se Entrega', 'Solimões', 2022),
    ...         Livro('Estrada da Vida', 'Rico', 2019),
    ...     ],
    ...     Busca(2014, 2018),
    ... )
    []

    >>> buscar_livros(
    ...     [
    ...         Livro('Frio da Madrugada', 'Solimões', 2021),
    ...         Livro('A Gente se Entrega', 'Solimões', 2022),
    ...         Livro('Estrada da Vida', 'Rico', 2019),
    ...     ],
    ...     Busca(2022, 2026),
    ... )
    [Livro(titulo='A Gente se Entrega', sobrenome='Solimões', ano=2022)]
    """

    lista_busca: list[Livro] = []

    for livro in livros:
        if livro.ano >= busca.ano_min and livro.ano <= busca.ano_max:
            lista_busca.append(livro)

    return lista_busca


# ===================================================================================================

# Exercício 2

# Análise
# Analisa uma lista de faturamentos de um período, e verifica quantos dias "memoráveis" há na lista.
# Um dia "memorável" é aquele que no qual o faturamento é maior que todos os faturamentos anteriores.
#
# Tipos de dados
# uma lista de faturamentos, ou seja, com valores floats e retorna um inteiro com a quantidade
# de dias "memoráveis".


def dias_memoraveis(faturamentos: list[float]) -> int:
    """
    Conta quantos dias "memoráveis" há em *faturamentos*, isto é, conta-se um dia
    "memorável" quando o faturamento de determinado dia é maior que todos os faturamentos
    dos dias anteriores. Obs: o primeiro dia é sempre memorável

    Exemplos
    >>> dias_memoraveis([96, 109, 99, 100, 109, 87, 120, 121])
    4
    >>> dias_memoraveis([96, 95, 95, 95, 94, 87])
    1
    >>> dias_memoraveis([230])
    1
    >>> dias_memoraveis([96, 109, 99, 100, 109, 87, 120, 198, 212, 121])
    5
    >>> dias_memoraveis([96, 109])
    2
    """

    contador_dias: int = 1

    for i in range(1, len(faturamentos)):
        eh_maior: bool = True
        j: int = 0
        while j < i and eh_maior:
            if faturamentos[i] > faturamentos[j]:
                eh_maior = True
            else:
                eh_maior = False
            j = j + 1
        if eh_maior:
            contador_dias = contador_dias + 1

    return contador_dias

