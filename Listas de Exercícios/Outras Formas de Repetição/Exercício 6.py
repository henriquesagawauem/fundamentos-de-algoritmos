# Rastreamento e retorno da função f([15, -3, 7, -1, 3])

# Esta função soma todos os números maiores que zero da lista e, em seguida, conta quantos dígitos matemáticos essa soma possui.

#     Soma dos positivos: 15 + 7 + 3 = 25 (a = 25)

#     Quantidade de dígitos de 25: 2 dígitos (b = 2)

# Ordem exata de execução das linhas:

#     Chamada da função e inicialização: 1, 2

#     Iteração x = 15: 3, 4, 5

#     Iteração x = -3: 3, 4

#     Iteração x = 7: 3, 4, 5

#     Iteração x = -1: 3, 4

#     Iteração x = 3: 3, 4, 5

#     Fim do for e preparação do while: 3, 6

#     Iteração do while com a = 25: 7, 8, 9 (agora a vale 2, b vale 1)

#     Iteração do while com a = 2: 7, 8, 9 (agora a vale 0, b vale 2)

#     Teste falso do while e retorno: 7, 10

# Ordem completa separada por vírgulas:
# 1, 2, 3, 4, 5, 3, 4, 3, 4, 5, 3, 4, 3, 4, 5, 3, 6, 7, 8, 9, 7, 8, 9, 7, 10

# Valor retornado: 2