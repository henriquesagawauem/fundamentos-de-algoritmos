# 26) As operações de módulo e divisão inteira são bastantes comuns na computação, mas muitos ainda
# não estão acostumados com essas operações, por isso é importante fazermos alguns exemplos para nos
# familiarizarmos com elas.
# a. Projete uma função que calcule a unidade de um número inteiro positivo, por exemplo, para o
# número 152, a unidade é 2.
# b. Projete uma função que calcule a dezena de um número inteiro positivo, por exemplo, para o
# número 152, a dezena é 5.
# c. Projete uma função que calcule a centena de um número inteiro positivo, por exemplo, para o
# número 152, a centena é 1.
# d. Projete uma função que verifique se os dois últimos dígitos de um número são 00.

# unidade(152) -> 2

def unidade(n: int) -> int:
    return n % 10

# dezena(152) -> 5

def dezena(n: int) -> int:
    return (n // 10) % 10

# centena(152) -> 1

def centena(n: int) -> int:
    return (n // 100) % 10

# termina_com_00(1200) -> True
# termina_com_00(152) -> False

def termina_com_00(n: int) -> bool:
    return n % 100 == 0