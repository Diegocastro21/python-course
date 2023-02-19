planetas = {'Jupiter', 'Marte', 'Venus'}
print(planetas)

# largo
print(len(planetas))

# agregar un elemento
planetas.add('Pluton')
print(planetas)
# Eliminar
planetas.remove('Marte') # Puede generar error si no se encuentra el elemento a eliminar
print(planetas)
# Eliminar sin error
planetas.discard('Jupiter')
print(planetas)
# Limpiar el set
planetas.clear()
print(planetas)
# Eliminar el set
del planetas