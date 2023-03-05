from Monitor import Monitor
from Teclado import Teclado
from Raton import Raton


class Computadora:
    contadorComputadora = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contadorComputadora += 1
        self._idComputadora = Computadora.contadorComputadora
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @property
    def raton(self):
        return self._raton

    @raton.setter
    def raton(self, raton):
        self._raton = raton

    def __str__(self):
        return f'''Computadora:[ ID: {self._idComputadora}
            Nombre: {self._nombre}
            {self._monitor}
            {self._teclado}
            {self._raton}
            ]
        '''

if __name__ == '__main__':
    raton = Raton('USB', 'Huawei')
    raton2 = Raton('Bluetooh', 'Samsung')
    monitor = Monitor('Dell', '16 Pulgadas')
    monitor2 = Monitor('LG', '22 Pulgadas')
    teclado = Teclado('USB', 'Huawei')
    teclado2 = Teclado('Bluetooh', 'Samsung')

    computadora1 = Computadora('Gateway', monitor, teclado, raton)
    computadora2 = Computadora('Lenovo', monitor2, teclado2, raton2)
    print(computadora1)
    print(computadora2)
