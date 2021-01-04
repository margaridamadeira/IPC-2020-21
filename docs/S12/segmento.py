# -*- coding: utf-8 -*-

"""
A classe Segmento
(c) Margarida Madeira e Moura, 2021

"""
from ponto import Ponto

class Segmento(Ponto):
    """Um segmento de reta, definido a partir de dois pontos no espaço cartesiano"""

    def __init__(self, A, B):
        self.A = A
        self.B = B
    
    def __str__(self):
        return('A: ' + str(self.A)+ ' B: ' + str(self.B))

    def length(self):
        return(self.A.distancia(self.B))

if __name__ == '__main__':
    P = Ponto()
    Q = Ponto(3,4)
    print(P.distancia(Q))

    s = Segmento(Ponto(), Ponto(3,4))
    print(s)
    print(s.length())
