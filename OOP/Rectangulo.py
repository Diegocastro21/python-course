class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


base = int(input('Proporcione la base: '))
altura = int(input('Proporcione la altura: '))

rectangulo = Rectangulo(base, altura)
print(f'Area del rectangulo: {rectangulo.area()}')