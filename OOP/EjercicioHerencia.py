class Vehicle:

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Vehiculo: [Color: {self.color}, Ruedas: {self.ruedas}]'


vehicle = Vehicle('red', 2)
print(vehicle)


class Coche(Vehicle):

    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'Vehiculo: [{super().__str__()}, Velocidad: {self.velocidad} km/hr]'

coche = Coche('blue', 4, 180)
print(coche)

class Bicicleta(Vehicle):

    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'Bicicleta: [{super().__str__()}, Tipo: {self.tipo}]'

bicicleta = Bicicleta('yellow', 2, 'Mountain')
print(bicicleta)