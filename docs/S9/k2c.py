# -*- coding: utf-8 -*-

"""
kelvin para celsius
(c) Margarida Madeira e Moura, 2020
"""

def k2c(kelvins: float) -> float:
    """Função que converte uma temperatura de kelvin para celsius.
    
    Exemplos:
        >>> k2c(273.15)
        0.0
        >>> k2c(268.15)
        -5.0  
            
    """

    resultado = kelvins - 273.15
    return resultado 

def test_k2c():
    x = float(input())
    z = k2c(x)
    print(z)
    
if __name__ == '__main__':
    test_k2c()

