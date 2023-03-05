from Monitor import Monitor
from Teclado import Teclado
from Raton import Raton
from Computadora import Computadora

class Orden:

    contadorOrdenes = 0

    def __init__(self, computadoras):
        Orden.contadorOrdenes += 1
        self._idOrden = Orden.contadorOrdenes
        self._computadoras = list(computadoras)


    def agregarComputadora(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ''
        for computadora in self._computadoras:
            computadoras_str += '\n' + computadora.__str__()
        return f'Orden: {self._idOrden}, {computadoras_str}'

if __name__ == '__main__':
    raton = Raton('USB', 'Huawei')
    raton2 = Raton('Bluetooh', 'Samsung')
    monitor = Monitor('Dell', '16 Pulgadas')
    monitor2 = Monitor('LG', '22 Pulgadas')
    teclado = Teclado('USB', 'Huawei')
    teclado2 = Teclado('Bluetooh', 'Samsung')
    computadora1 = Computadora('Gateway', monitor, teclado, raton)
    computadora2 = Computadora('Lenovo', monitor2, teclado2, raton2)

    computadora3 = Computadora('Huawei', monitor2, teclado, raton2)
    computadora4 = Computadora('Samsung', monitor2, teclado, raton)

    computadoras = [computadora1, computadora2]
    computadoras2 = [computadora3, computadora4]

    orden1 = Orden(computadoras)
    orden2 = Orden(computadoras2)

    print(orden1)
    print(orden2)

    computadora5 = Computadora('Macbook', monitor2, teclado2, raton)
    orden1.agregarComputadora(computadora5)

    print('Se agrego otra computadora'.center(60, '-'))
    print(orden1)



