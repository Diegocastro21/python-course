from GeometricFigure import GeometricFigure
from Color import Color


class Rectangulo(GeometricFigure, Color):

    def __init__(self, alto, ancho, color):
        GeometricFigure.__init__(self, alto, ancho)
        Color.__init__(self, color)

    def area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'Rectangulo: [{GeometricFigure.__str__(self)} {Color.__str__(self)}]'
