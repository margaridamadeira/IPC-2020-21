# -*- coding: utf-8 -*-

"""
celsius para farenheit
(c) Margarida Madeira e Moura, 2020
"""

def c2f(celsius: float) -> float:
    """Função que converte uma temperatura de celsius para farenheit

    Exemplos:
        >>> c2f(100.0)
        212.0
        >>> k2c(0.0)
        32.0
    """

    resultado = (celsius * 1.8) + 32
    return resultado 

def test_c2f():
    x = float(input())
    z = c2f(x)
    print(z)
    
if __name__ == '__main__':
    test_c2f()


