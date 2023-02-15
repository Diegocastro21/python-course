# sintaxis de range(inicio<opcional>, final<requerido>, incremento<opcional>)

print('Ejercicio 01: Recorrer un rango de 0 al 10 solo numero divisibles entre 3')
for i in range(0, 11, +1):
    if i % 3 == 0:
        print(i)

print('Ejercicio 02: Crear Un rango de numeros de 2 a 6, e imprimirlos')
for i in range(2, 6+1, +1):
    print(i)

print('Ejercicio 03: Crear un rango de 3 a 10. pero con incremento de 2 en 2')

for i in range(3, 10, +2):
    print(i)