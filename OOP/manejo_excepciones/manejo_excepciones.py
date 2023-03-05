from NumerosIdenticosException import NumerosIdenticosException
resultado = None

try:
    a = int(input('ingrese un numero: '))
    b = int(input('ingrese otro numero: '))

    if a == b:
        raise NumerosIdenticosException('Numeros Identicos')

    resultado = a / b
except ZeroDivisionError as e:
    print(f'ZeroDivisonError - Ocurrio un error: {e}, {type(e)}')
except TypeError as e:
    print(f'TypeError - Ocurrio un error: {e}, {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrio un error: {e}, {type(e)}')
else:
    print(f'Bloque else por si no se presenta ninguna exception')
finally:
    print(f'Bloque finally que se ejecuta independiente de si hay o no exception')

print(f'Resultado: {resultado}')
print('Continuamos')
