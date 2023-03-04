class Aritmetica:

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB


aritmetica1 = Aritmetica(5, 3)

print(f'''sumar: {aritmetica1.sumar()}
restar: {aritmetica1.restar()}
multiplicar: {aritmetica1.multiplicar()}
dividir: {aritmetica1.dividir(): .2f}
''')

