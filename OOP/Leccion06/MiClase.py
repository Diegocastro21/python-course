class MiClase:

    variable_clase = '--| Mi variable de clase |--'

    def __init__(self, variable_de_instancia):
        self.variable_de_instancia = variable_de_instancia

    @staticmethod
    def metodo_estatico():
        print(f'Desde el metodo estatico {MiClase.variable_clase}')

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_de_instancia)



MiClase.metodo_estatico()
MiClase.metodo_clase()
print(MiClase.variable_clase)
miclase = MiClase('Valor de variable de instancia')
print(miclase.variable_de_instancia, miclase.variable_clase)

# podemos accionar variables de clase
# al vuelo= en cualquier momento
MiClase.variable_clase2 = 'Mi segunda varibale de clase'


miclase02 = MiClase('Valorsito Instancia')
print(miclase02.variable_de_instancia, miclase.variable_clase)
print(miclase.variable_clase2)

print("Probando Metodos de instacia".center(50, "+"))
miclase02.metodo_instancia()
