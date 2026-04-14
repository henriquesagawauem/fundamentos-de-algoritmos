# Henrique Tutomu Sagawa - 152725

# Atividade 01

# Análise
# Calcular a quantidade de balas que a loja está comprando com base
# na quantidade de balas por caixas e pacotes avulsos, onde cada caixa
# tem 15 pacotes, e cada pacote tem 40 balas.
#
# Tipos de dados
# Número de caixas e pacotes no formato int e retornar um número
# de balas, também no formato int. Todos os valores são representados
# por números positivos.


def entr_estoque(qt_caixas: int, qt_pacotes: int) -> int:
    """
    Calcula o total de unidades que serão acrescentadas no estoque
    do produto considerando que serão compradas *qt_caixas* de 15
    pacotes e ainda *qt_pacotes*, onde cada pacote tem 40 balas.

    Exemplos
    >>> # ((2 * 15) * 40) + 1 * 40
    >>> entr_estoque(2, 1)
    1240
    >>> # ((1 * 15) * 40) + 0 * 40
    >>> entr_estoque(1, 0)
    600
    >>> # ((0 * 15) * 40) + 1 * 40
    >>> entr_estoque(0, 1)
    40
    """

    balas_por_caixa: int = (qt_caixas * 15) * 40
    balas_por_pacote: int = qt_pacotes * 40
    return balas_por_caixa + balas_por_pacote


# ==========================================================================

# Atividade 02

# Análise
# Verificar se em um nome completo fornecido pelo usuário
# o primeiro nome é igual a um nome fornecido pelo usuário, e o
# nome completo não possui espaços em branco no começo e no fim
#
# Tipos de dados
# Um nome completo no formato string que contenha pelo menos
# um espaço em branco separando o nome e sobrenome. Também um outro
# nome no formato string para a verificação.


def verificarNome(nomeCompleto: str, nome: str) -> bool:
    """
    Recebe o *nomeCompleto* e verifica se o primeiro nome é
    igual a *nome*. Em *nomeCompleto* há pelo menos um espaço
    em branco separando o nome e sobrenome e não possui espaços em
    branco no início e no fim

    Exemplos
    >>> verificarNome("Neymar Junior", "Neymar")
    True
    >>> verificarNome("Neymar do Santos Junior", "Sandro")
    False
    >>> verificarNome("Carlos Palmeiras da Silva", "Carlos")
    True
    >>> verificarNome("Luis Felipe Saar", "luis")
    True
    >>> verificarNome("Pele da Silva", "Messi")
    False
    """

    return nomeCompleto[: len(nome)].lower() == nome.lower()


# ========================================================================

# Atividade 03


# Análise
# Formatar o sobrenome e o ano informado pelo usuário para
# o formato de citação ABNT (SOBRENOME, ano), onde o sobrenome deve ter todos
# os seus caracteres maiúsculos.
#
# Tipos de dados
# Sobrenome do autor no formato String, e o ano no formato int
# e retornar um valor no formato String


def formatarAbnt(sobrenome: str, ano: int) -> str:
    """
    Formatar o sobrenome do autor e o ano fornecido pelo usuário
    para o formato padrão de citação ABNT, sendo ele, (SOBRENOME, ano), onde
    o sobrenome deve obrigatóriamente ter todos os seus caracteres
    maiúsculos.

    Exemplos
    >>> formatarAbnt("silva", 2017)
    '(SILVA, 2017)'
    >>> formatarAbnt("Abacate", 2024)
    '(ABACATE, 2024)'
    >>> formatarAbnt("Palmeiras", 1914)
    '(PALMEIRAS, 1914)'
    >>> formatarAbnt("Stewart", 2017)
    '(STEWART, 2017)'
    >>> formatarAbnt("Guidorizzi", 1983)
    '(GUIDORIZZI, 1983)'
    """

    return "(" + sobrenome.upper() + ", " + str(ano) + ")"
