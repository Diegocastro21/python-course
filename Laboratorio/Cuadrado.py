from GeometricFigure import GeometricFigure
from Color import Color


class Cuadrado(GeometricFigure, Color):

    def __init__(self, lado, color):
        GeometricFigure.__init__(self, lado, lado)
        Color.__init__(self, color)

    def area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'Cuadrado: [{GeometricFigure.__str__(self)} {Color.__str__(self)}]'
