class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):
        return f'{self.nombre} {other.nombre}'

    def __sub__(self, other):
        return self.edad - other.edad

persona01 = Persona('Fulanito', 28)
persona02 = Persona('De tal', 20)
print(persona02 + persona01)
print(persona01 - persona02)
