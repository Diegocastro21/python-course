# Definir una tupla
frutas = ('Naranja', 'Platano', 'Guayaba')
print(frutas)
# Saber el rango
print(len(frutas))
# Acceder a un elemento
print(frutas[0])
# Acceder con navegacion inversa
print(frutas[-1])
# Acceder a un rango de valores
print(frutas[:2]) # sin incluir el ultimo indice

# Recorrer elementos de una tupla
for fruta in frutas:
    print(fruta)

# Para imprimir en una sola linea
for fruta in frutas:
    print(fruta, end=' ')

print(' ')

# Cambiar el valor de una tupla
# frutas[0] = 'Pera' no se puede por que las tuplas son inmutables
# haciendo la conversion de una tupla a una lista
frutasLista = list(frutas)
frutasLista[0] = 'Pera'
frutas = tuple(frutasLista)
print(frutas)
# Eliminar la tupla por completo
del frutas