def multiplicar(*args):
    resultado = 1
    for valor in args:
        resultado *= valor

    return resultado

print(float(multiplicar(1,2,3,4,5,6,7,8,9)))
print(multiplicar(1,3,5))