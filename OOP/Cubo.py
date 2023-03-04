class Cubo:

    def __init__(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad

    def volumen(self):
        return self.ancho * self.altura * self.profundidad

ancho = int(input('Proporciona el ancho: '))
altura = int(input('Proporciona la altura: '))
profundidad = int(input('Proporciona la profundidad: '))

cubo = Cubo(ancho, altura, profundidad)

print(f'Volumen Del Cubo: {cubo.volumen()}')
