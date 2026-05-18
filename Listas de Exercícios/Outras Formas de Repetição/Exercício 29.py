from dataclasses import dataclass


@dataclass
class Fruta:
    nome: str
    receita: float


def maior(lista: list[Fruta]) -> list[Fruta]:
    if len(lista) <= 1:
        return lista
    pivo: Fruta = lista[0]
    menores = []
    maiores = []

    for i in lista[1:]:
        if i.receita <= pivo.receita:
            menores.append(i)
        elif i.receita > pivo.receita:
            maiores.append(i)

    return maior(menores) + [pivo] + maior(maiores)
