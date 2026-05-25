from enum import Enum, auto
from dataclasses import dataclass


class Pagamento(Enum):
    DINHEIRO = auto()
    PIX = auto()
    CARTAO = auto()


@dataclass
class Venda:
    nome: str
    valor: float
    forma: Pagamento


@dataclass
class Desempenho:
    valor: float
    vendas: int
    comissao: float


def calc_desempenho(vendas: list[Venda], nome: str) -> Desempenho:
    """
    >>> calc_desempenho(vendas_teste, 'Ana')
    Desempenho(valor=14555.0, vendas=20, comissao=480.75000000000006)
    """

    # Procura a venda pelo nome do funcionário

    vendas_func: list[Venda] = []

    for venda in vendas:
        if venda.nome == nome:
            vendas_func.append(venda)

    # Calcula o valor de suas vendas

    valor: float = 0
    for venda in vendas_func:
        valor = valor + venda.valor

    # Calcula o número de vendas
    num_vendas = len(vendas_func)

    # Calcula a comissão do funcionário
    comissao: float = 0
    for venda in vendas_func:
        if venda.forma == Pagamento.PIX or venda.forma == Pagamento.DINHEIRO:
            comissao = comissao + (venda.valor * 0.05)
        elif venda.forma == Pagamento.CARTAO:
            comissao = comissao + (venda.valor * 0.03)

    return Desempenho(valor, num_vendas, comissao)


# Lista de vendas volumosa para testes
vendas_teste = [
    Venda('Ana', 150.00, Pagamento.PIX),
    Venda('Bruno', 2500.50, Pagamento.CARTAO),
    Venda('Carlos', 45.90, Pagamento.DINHEIRO),
    Venda('Daniela', 899.90, Pagamento.CARTAO),
    Venda('Eduardo', 120.00, Pagamento.PIX),
    Venda('Ana', 340.00, Pagamento.CARTAO),
    Venda('Bruno', 15.00, Pagamento.DINHEIRO),
    Venda('Carlos', 1250.00, Pagamento.PIX),
    Venda('Daniela', 450.00, Pagamento.DINHEIRO),
    Venda('Eduardo', 310.50, Pagamento.CARTAO),
    Venda('Ana', 85.00, Pagamento.DINHEIRO),
    Venda('Bruno', 99.90, Pagamento.PIX),
    Venda('Carlos', 2300.00, Pagamento.CARTAO),
    Venda('Daniela', 1500.00, Pagamento.PIX),
    Venda('Eduardo', 60.00, Pagamento.DINHEIRO),
    Venda('Ana', 1050.00, Pagamento.CARTAO),
    Venda('Bruno', 420.00, Pagamento.PIX),
    Venda('Carlos', 310.00, Pagamento.DINHEIRO),
    Venda('Daniela', 75.50, Pagamento.CARTAO),
    Venda('Eduardo', 1800.00, Pagamento.PIX),
    Venda('Ana', 220.00, Pagamento.PIX),
    Venda('Bruno', 1350.00, Pagamento.CARTAO),
    Venda('Carlos', 95.00, Pagamento.DINHEIRO),
    Venda('Daniela', 540.00, Pagamento.CARTAO),
    Venda('Eduardo', 410.00, Pagamento.PIX),
    Venda('Ana', 670.00, Pagamento.CARTAO),
    Venda('Bruno', 55.00, Pagamento.DINHEIRO),
    Venda('Carlos', 1650.00, Pagamento.PIX),
    Venda('Daniela', 230.00, Pagamento.DINHEIRO),
    Venda('Eduardo', 890.00, Pagamento.CARTAO),
    Venda('Ana', 125.00, Pagamento.DINHEIRO),
    Venda('Bruno', 340.00, Pagamento.PIX),
    Venda('Carlos', 4100.00, Pagamento.CARTAO),
    Venda('Daniela', 950.00, Pagamento.PIX),
    Venda('Eduardo', 75.00, Pagamento.DINHEIRO),
    Venda('Ana', 2150.00, Pagamento.CARTAO),
    Venda('Bruno', 620.00, Pagamento.PIX),
    Venda('Carlos', 180.00, Pagamento.DINHEIRO),
    Venda('Daniela', 120.00, Pagamento.CARTAO),
    Venda('Eduardo', 2450.00, Pagamento.PIX),
    Venda('Ana', 310.00, Pagamento.PIX),
    Venda('Bruno', 850.00, Pagamento.CARTAO),
    Venda('Carlos', 65.00, Pagamento.DINHEIRO),
    Venda('Daniela', 310.00, Pagamento.CARTAO),
    Venda('Eduardo', 520.00, Pagamento.PIX),
    Venda('Ana', 780.00, Pagamento.CARTAO),
    Venda('Bruno', 45.00, Pagamento.DINHEIRO),
    Venda('Carlos', 1150.00, Pagamento.PIX),
    Venda('Daniela', 620.00, Pagamento.DINHEIRO),
    Venda('Eduardo', 1340.00, Pagamento.CARTAO),
    Venda('Ana', 95.00, Pagamento.DINHEIRO),
    Venda('Bruno', 180.00, Pagamento.PIX),
    Venda('Carlos', 2900.00, Pagamento.CARTAO),
    Venda('Daniela', 1100.00, Pagamento.PIX),
    Venda('Eduardo', 85.00, Pagamento.DINHEIRO),
    Venda('Ana', 1650.00, Pagamento.CARTAO),
    Venda('Bruno', 730.00, Pagamento.PIX),
    Venda('Carlos', 240.00, Pagamento.DINHEIRO),
    Venda('Daniela', 95.00, Pagamento.CARTAO),
    Venda('Eduardo', 1950.00, Pagamento.PIX),
    Venda('Ana', 430.00, Pagamento.PIX),
    Venda('Bruno', 1100.00, Pagamento.CARTAO),
    Venda('Carlos', 115.00, Pagamento.DINHEIRO),
    Venda('Daniela', 420.00, Pagamento.CARTAO),
    Venda('Eduardo', 670.00, Pagamento.PIX),
    Venda('Ana', 890.00, Pagamento.CARTAO),
    Venda('Bruno', 35.00, Pagamento.DINHEIRO),
    Venda('Carlos', 1420.00, Pagamento.PIX),
    Venda('Daniela', 180.00, Pagamento.DINHEIRO),
    Venda('Eduardo', 920.00, Pagamento.CARTAO),
    Venda('Ana', 160.00, Pagamento.DINHEIRO),
    Venda('Bruno', 290.00, Pagamento.PIX),
    Venda('Carlos', 3400.00, Pagamento.CARTAO),
    Venda('Daniela', 820.00, Pagamento.PIX),
    Venda('Eduardo', 95.00, Pagamento.DINHEIRO),
    Venda('Ana', 2500.00, Pagamento.CARTAO),
    Venda('Bruno', 510.00, Pagamento.PIX),
    Venda('Carlos', 130.00, Pagamento.DINHEIRO),
    Venda('Daniela', 240.00, Pagamento.CARTAO),
    Venda('Eduardo', 3100.00, Pagamento.PIX),
    Venda('Ana', 520.00, Pagamento.PIX),
    Venda('Bruno', 930.00, Pagamento.CARTAO),
    Venda('Carlos', 75.00, Pagamento.DINHEIRO),
    Venda('Daniela', 510.00, Pagamento.CARTAO),
    Venda('Eduardo', 380.00, Pagamento.PIX),
    Venda('Ana', 920.00, Pagamento.CARTAO),
    Venda('Bruno', 65.00, Pagamento.DINHEIRO),
    Venda('Carlos', 1850.00, Pagamento.PIX),
    Venda('Daniela', 730.00, Pagamento.DINHEIRO),
    Venda('Eduardo', 1150.00, Pagamento.CARTAO),
    Venda('Ana', 110.00, Pagamento.DINHEIRO),
    Venda('Bruno', 430.00, Pagamento.PIX),
    Venda('Carlos', 1750.00, Pagamento.CARTAO),
    Venda('Daniela', 1350.00, Pagamento.PIX),
    Venda('Eduardo', 55.00, Pagamento.DINHEIRO),
    Venda('Ana', 1400.00, Pagamento.CARTAO),
    Venda('Bruno', 820.00, Pagamento.PIX),
    Venda('Carlos', 320.00, Pagamento.DINHEIRO),
    Venda('Daniela', 165.00, Pagamento.CARTAO),
    Venda('Eduardo', 2100.00, Pagamento.PIX),
]