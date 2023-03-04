class Persona:

    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def mostrar_detalles(self):
        print(f' {self._nombre} {self.apellido} {self.edad}')

persona = Persona('Juan', 'Perez', 28)
print(persona.nombre)
persona.nombre = 'Juanito Alimana'
print(persona.nombre)

