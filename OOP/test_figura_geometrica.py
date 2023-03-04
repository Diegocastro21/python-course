from Cuadrado import Cuadrado

cuadrado = Cuadrado(5, 'Green')
print(cuadrado.ancho, cuadrado.alto)
print(cuadrado.color)
print(cuadrado.calcular_area())

print(Cuadrado.mro())