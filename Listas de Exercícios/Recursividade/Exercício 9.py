def par(n: int) -> bool:
    """
    Verifica se *n* é par

    Exemplos
    >>> par(3)
    False
    >>> par(2)
    True
    """
    resultado  = False

    if n == 0:
        resultado = True
    else:
        resultado = impar(n - 1)
    
    return resultado

def impar(n: int) -> bool:
    """
    Verifica se *n* é impar

    >>> impar(3)
    True
    >>> impar(2)
    False
    """
    resultado = True
    
    if n == 0:
        resultado = False
    else:
        resultado = par(n - 1)
    
    return resultado
