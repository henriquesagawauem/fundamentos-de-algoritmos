def encontra_maior(lista: list[int]) -> int:
    maior = 0
    if len(lista) == 1:
        maior = lista[0]
    else:
        maior2 = encontra_maior(lista[1:])

        if lista[0] > maior2:
            maior = lista[0]
        else:
            maior = maior2

    return maior
