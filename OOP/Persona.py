class Persona:

    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')

    def __del__(self):
        print(f'Persona Eliminada: {self._nombre} {self._apellido}')


if __name__ == '__main__':
    persona = Persona('Juan', 'Perez', 28)
    print(persona.nombre)
    # manda a llamar indirectamente el metodo set persona.nombre = '  '
    # manda a llamar indirectamente el metodo get persona.nombre
    persona.nombre = 'Fulanito de tal'
    persona.apellido = 'Maria la baja'
    persona.edad = 32
    persona.mostrar_detalles()
