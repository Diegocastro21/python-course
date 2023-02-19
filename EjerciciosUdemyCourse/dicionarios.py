# dict (key, value)
diccionario = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}

print(diccionario)
# Largo del diccionario
print(len(diccionario))
# acceder a un elemento (key)
print(diccionario['IDE'])
# Otra forma de acceder a un elemento
print(diccionario.get('OOP'))
# Modificando elementos
diccionario['IDE'] = 'integrated development environment'
print(diccionario)

# Recorrer los diccionarios
for termino, valor in diccionario.items():
    print(termino, valor)
for termino in diccionario.keys():
    print(termino)
for valor in diccionario.values():
    print(valor)
# Existencia de un elemento en un diccionario
print('IDE' in diccionario)
# Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Remover un elemento
diccionario.pop('DBMS')
print(diccionario)

# Limpiar el diccionario
diccionario.clear()
print(diccionario)

# Eliminar el diccionario por completo
del diccionario
# print(diccionario) lanzara error
