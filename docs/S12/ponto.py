# -*- coding: utf-8 -*-

"""
A classe Ponto
(c) Margarida Madeira e Moura, 2021
"""

class Ponto:
    """Um ponto no espaço cartesiano"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return('x = ' + str(self.x) + ' y = ' + str(self.y))

    def imprimir(self):
        print('x =', self.x, 'y =', self.y)

    def distancia(self, outroPonto):
        """Distância entre dois pontos"""
        dist_x = self.x - outroPonto.x
        dist_y = self.y - outroPonto.y
        resultado = (dist_x**2 + dist_y**2)**0.5
        return(resultado)

if __name__ == '__main__':
    p = Ponto()
    q = Ponto(3, 4)

    p.imprimir()
    print(q)

    print(p.distancia(q))
