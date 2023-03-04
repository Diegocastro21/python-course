from Rectangulo import Rectangulo
from Cuadrado import Cuadrado

# no se puede instanciar una clase abstracta
# figura = FiguraGeometrica()

print('Creacion de Objeto Cuadrado'.center(80, '-'))
cuadrado = Cuadrado(lado=4, color='Pink')
print(cuadrado)
print(f'Area Del Cuadrado: {cuadrado.area()}')

print('Creacion de Objeto Rectangulo'.center(80, '-'))
rectangulo = Rectangulo(alto=7, ancho=9 ,color='Violet')
print(rectangulo)
print(f'Area Del Rectangulo: {rectangulo.area()}')