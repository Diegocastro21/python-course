nombres = ['Juan', 'Karla', 'Ricardo', 'Maria', 'franchesca', 'alberto']
# 1 Manera: [0]  ,   [1]  ,   [2]    ,   [3]  ,     [4]     ,     [5]
# 2 Manera: [-6]  ,   [-5]  ,   [-4]    ,   [-3]  ,     [-2]     ,     [-1]

# Acceder a los valores de la lista
print(nombres)

print(nombres[0])
print(nombres[1])

# acceder a los valores de manera inversa

print(nombres[-1])
print(nombres[-2])
print(nombres[-6])

# no incluye el elemento 3
print(nombres[0:3])
# Desde el inicio hasta el elemento 4 pero no lo incluye
print(nombres[:4])
# empieza desde el elemento 3 hasta el final
print(nombres[3:])

nombres[2] = 'Galera'
print(nombres)

for nombre in nombres:
    print(nombre)

print(f'''

---  Metodos Para Listas ---

''')
# Largo de una lista
print(f'''

Longitud len(__obj): {len(nombres)}

nombres.append('Lorenzo'): {nombres.append('Lorenzo')}
nombres.append(): {nombres}

Ingresar en una posicion determinada
nombres.insert(2, 'Fulanito de tal') {nombres.insert(2, 'Fulanito De Tal')}
nombres.insert(_index, 'Value') --> {nombres}

remover un elemento
nombres.remove('Fulanito De Tal') {nombres.remove('Fulanito De Tal')}
nombres.remove(_value) --> {nombres}

remover el ultimo elemento
nombres.pop()  {nombres.pop()}
nobres.pop() --> {nombres}
''')

# Eliminar en un indice indicado
print('Se elimino el elemento [3]')
del nombres[3]
print(nombres)

# Eliminar todos los elementos de nuetra lista
print('Limpiar todos los elementos de nuestra lista con nombres.clear()')
nombres.clear()
print(nombres)
# Borrar la lista por completo
print('del nombres')
del nombres
print('Se borro la lista por completo y \nno se puede acceder a ellas ')

