#ABC Abstract Base Class

from abc import ABC, abstractmethod

class GeometricFigure(ABC):
    def __init__(self, alto, ancho):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f'Valor Erroneo alto: {alto}')
            self._alto = 0

        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f'Valor Erroneo ancho: {ancho}')
            self._ancho = 0

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f'Valor Erroneo alto: {alto}')
            self._alto = 0

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f'Valor Erroneo ancho: {ancho}')
            self._ancho = 0

    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f'Figure Geometric: [ Alto: {self._alto}, Ancho: {self._ancho}]'

    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False
