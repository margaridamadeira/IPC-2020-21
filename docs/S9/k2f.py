# -*- coding: utf-8 -*-

"""
kelvin para farenheit, usando import
(c) Margarida Madeira e Moura, 2020
"""

from k2c import k2c
from c2f import c2f

def k2f(kelvins: float) -> float:
    """Função que converte uma temperatura de kelvin para farenheit.
    
    Exemplos:
    >>> k2f(273.15)
    32.0
    >>> k2f(373.15)
    212.0
    
    """
    return c2f(k2c(kelvins))


def test_k2f():
    x = float(input())
    z = k2f(x)
    print(z)
    
if __name__ == '__main__':
    test_k2f()
