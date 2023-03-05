from DispositivoEntrada import DispositivoEntrada as de


class Teclado(de):
    contadorTeclado = 0

    def __init__(self, tipoEntrada, marca):
        Teclado.contadorTeclado += 1
        self._idTeclado = Teclado.contadorTeclado
        de.__init__(self, tipoEntrada, marca)

    def __str__(self):
        return f'Teclado: [ID: {self._idTeclado} {de.__str__(self)}]'


if __name__ == '__main__':
    teclado = Teclado('USB', 'Huawei')
    teclado2 = Teclado('Bluetooh', 'Samsung')
    print(teclado)
    print(teclado2)