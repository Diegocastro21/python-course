# por buenas practicas si se usa argumentos variables
# recomienda usar *args
def sumar( *args):
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado


print(sumar(1,2,3,4,5,6,7,8,9))

# si no queremos agregar nuestra funcion todavia
# podemos usar la palabra pass