def caca_palavras(m: list[list[str]], s: str) -> int:
    contador = 0

    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == s[0]:
                if j + len(s) <= len(m[i]):
                    encontrou = True
                    k = 0
                    while k < len(s) and encontrou:
                        if m[i][j + k] != s[k]:
                            encontrou = False
                        k = k + 1
                    if encontrou:
                        contador = contador + 1
                if i + len(s) <= len(m):
                    encontrou = True
                    k = 0
                    while k < len(s) and encontrou:
                        if m[i + k][j] != s[k]:
                            encontrou = False
                        k = k + 1
                    if encontrou:
                        contador = contador + 1

    return contador


teste = [
    ['A', 'C', 'A', 'S', 'A', 'M', 'C', 'A', 'S', 'W', 'B'],
    ['C', 'A', 'X', 'R', 'F', 'T', 'P', 'A', 'S', 'A', 'C'],
    ['A', 'S', 'X', 'I', 'E', 'J', 'H', 'W', 'T', 'Q', 'A'],
    ['S', 'A', 'E', 'O', 'W', 'M', 'Q', 'Z', 'O', 'D', 'B'],
    ['A', 'C', 'Y', 'K', 'F', 'W', 'C', 'A', 'A', 'V', 'B'],
]