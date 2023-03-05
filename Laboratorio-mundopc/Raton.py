from DispositivoEntrada import DispositivoEntrada as de


class Raton(de):
    contadorRatones = 0

    def __init__(self, tipoEntrada, marca):
        Raton.contadorRatones += 1
        self._idRaton = Raton.contadorRatones
        de.__init__(self, tipoEntrada, marca)

    def __str__(self):
        return f'Raton: [ID: {self._idRaton} {de.__str__(self)}]'


if __name__ == '__main__':
    raton = Raton('USB', 'Huawei')
    raton2 = Raton('Bluetooh', 'Samsung')
    print(raton)
    print(raton2)