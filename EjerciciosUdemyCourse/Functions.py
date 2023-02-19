def mi_function():
    print('Funcion normalita sin parametros')


for f in range(10):
    print(f + 1, ' -->', end=' ')
    mi_function()


def mi_function2(nombre, apellido):
    print(f'My name\'s  {nombre} {apellido}')


mi_function2('Diego', 'Castro')
mi_function2('Karla', 'Jara')


def sumar(a, b):
    return a + b


resultado = sumar(3, 8)
print(resultado)


# valor por default en los parametros
# La sintaxis a:int es un pista de cual seria el posible tipo de dato
# -> int al final de una funcion tambien es una pista y puede ser redudante
def restar(a: int = 0, b: int = 0) -> int:
    return a - b


print(restar(4, 2))
print(restar(18, 23))


# Argumentos variables

def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)


listarNombres('Juanito', 'Felipito', 'Napoleon', 'Dinamarca', 'Escocia')


# Keyword arguments
def listarDiccionario(**kwargs):
    for llave, valor in kwargs.items():
        print(f' {llave}: {valor}')


listarDiccionario(IDE='Integrated Development Environment',
                  PK='Primary Key')


def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)


nombres = ['Juanito', 'Marciano', 'Espitaleta']
desplegarNombres(nombres)

# convertir valores int y que no son interables en una tupla
# genera error -> desplegarNombres(10, 11)
desplegarNombres((10, 11))
# para convertir a una lista se usa
desplegarNombres([12, 13])


# Funcion recursiva
# Mandar a llamar a un funcion asimisma
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

resultado = factorial(5)
print(f'factorial de 5 -> {resultado}')