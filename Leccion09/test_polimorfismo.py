from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto))
    if isinstance(objeto, gerente):
        print(objeto.departamento)


empleado = Empleado('Juan', 9000)
print(empleado)

gerente = Gerente('Karla', 6000, 'Sistemas')
print(gerente)
