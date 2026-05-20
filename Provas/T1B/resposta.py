# henrique-tutomu-sagawa-152725
# =================================================================================================

# Questão 1

from enum import Enum, auto
from dataclasses import dataclass

# Análise
# Informar entre dois produtos qual é o mais barato para comprar considerando que o cliente quer comprar um recipiente
#
# Tipos de dados
# dois produtos com informações de nome, sabor e o valor por cm cúbico em float e o volume da sobremesa em float, e retornará qual dos produtos sai mais barato, com todas as informações do produto.


@dataclass
class Produto:
    """
    Informações do produto com nome e sabor sendo uma string e o valor por cm cúbico em float e o volume da sobremesa em float
    """

    nome: str
    sabor: str
    valor_por_cm_3: float
    volume: float


def mais_barato(p1: Produto, p2: Produto) -> Produto:
    """
    Informar entre o *p1* e o *p2* qual sai mais barato para a compra, considerando que o cliente quer
    comprar um recipiente, onde cada sobremesa tem um recipiente de no máximo 20 cm cúbicos e a Dona Tereza
    sabe o valor por cm cúbico de cada sobremesa.

    Exemplos
    >>> mais_barato(
    ...     Produto('Bolo', 'Chocolate', 23.30, 4), Produto('Bolo', 'Morango', 17.70, 1)
    ... )
    Produto(nome='Bolo', sabor='Morango', valor_por_cm_3=17.7, volume=1)
    >>> mais_barato(
    ...     Produto('Torta', 'Chocolate', 13.97, 12),
    ...     Produto('Bolo', 'Strogonoff', 19.26, 12),
    ... )
    Produto(nome='Torta', sabor='Chocolate', valor_por_cm_3=13.97, volume=12)
    >>> mais_barato(
    ...     Produto('Pudim', 'Doce de Leite', 29.30, 20),
    ...     Produto('Pudim', 'Uva', 12.99, 1),
    ... )
    Produto(nome='Pudim', sabor='Uva', valor_por_cm_3=12.99, volume=1)
    """
    assert p1.volume > 0 and p1.volume <= 20 and p2.volume > 0 and p2.volume <= 20, (
        'O volume da sobremesa deve ser pelo menos 1 e não pode ser maior que 20'
    )

    if p1.valor_por_cm_3 * p1.volume <= p2.valor_por_cm_3 * p2.volume:
        return p1

    return p2


# ==========================================================================================================

# Questão 2

# Análise
# Calcular o preço da venda de um pastel baseando-se no preço base, sabor de pastel, tamanho do pastel e a opção
# de adicionar molho especial
#
# Tipos de dados
# Informações do pastel, como sabor (queijo, carne, frango ou carne com ovo), tamanho do pastel (mini,
# normal ou grande) e adicional de molho especial (um booleano "true" ou "false", "sim" ou "não"), e a função
# retorna um float com o valor total da venda do pastel.


class Sabor(Enum):
    """
    Todos os sabores de pastéis à venda na pastelaria (queijo, carne, frango, carne com ovo)
    """

    QUEIJO = auto()
    CARNE = auto()
    FRANGO = auto()
    CARNE_COM_OVO = auto()


class Tamanho(Enum):
    """
    Todos os tamanhos de pastéis à venda na pastelaria (mini, normal, grande)
    """

    MINI = auto()
    NORMAL = auto()
    GRANDE = auto()


@dataclass
class Pastel:
    """
    Informações do pastel, como sabor, tendo o tipo 'Sabor', tamanho, tendo o tipo 'Tamanho' e
    opção de pedir com ou sem molho especial, sendo um 'booleano' ('true' ou 'false' | 'sim' ou 'não')
    """

    sabor: Sabor
    tamanho: Tamanho
    com_molho: bool


def calc_pastel(p: Pastel) -> float:
    """
    Calcula o preço da venda de um pastel baseado nas informações de *p*, podendo varias os valores por conta de
    sabor, tamanho e molho, onde cada sabor tem um valor adicinal, cada tamanho tem um acréscimo e também haverá
    um acréscimo se o cliente optar por adicionar molho especial.

    Exemplos
    >>> # ((10 + 2) * 1.1)
    >>> calc_pastel(Pastel(Sabor.QUEIJO, Tamanho.MINI, False))
    13.200000000000001
    >>> # ((10 + 2) * 1.1) + 3
    >>> calc_pastel(Pastel(Sabor.QUEIJO, Tamanho.MINI, True))
    16.200000000000003
    >>> # ((10 + 5) * 1.3) + 3
    >>> calc_pastel(Pastel(Sabor.FRANGO, Tamanho.GRANDE, True))
    22.5
    >>> # ((10 + 7) * 1.2)
    >>> calc_pastel(Pastel(Sabor.CARNE_COM_OVO, Tamanho.NORMAL, False))
    20.4
    """

    valor: float = 10

    if p.sabor == Sabor.QUEIJO:
        valor = valor + 2
    elif p.sabor == Sabor.CARNE:
        valor = valor + 4
    elif p.sabor == Sabor.FRANGO:
        valor = valor + 5
    elif p.sabor == Sabor.CARNE_COM_OVO:
        valor = valor + 7

    if p.tamanho == Tamanho.MINI:
        valor = valor * 1.1
    elif p.tamanho == Tamanho.NORMAL:
        valor = valor * 1.2
    elif p.tamanho == Tamanho.GRANDE:
        valor = valor * 1.3

    if p.com_molho:
        valor = valor + 3

    return valor