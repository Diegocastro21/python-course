maximo = 5
condicion = 0

while condicion <= maximo:
    print(condicion)
    condicion += 1

print('------------------------')
minimo = 1
while condicion >= minimo:
    print(condicion)
    condicion -= 1

print('------------------------')

cadena = 'Hola Mundo En Python'

for letra in cadena:
    print(letra)
else:
    print('Fin Ciclo For')
    print(f'''
    Se Termino Esta vaina
    
''')

for letraa in 'Holanda':
    if letraa == 'a':
        print(f'Letra encontrada: {letraa}')
        break
#         Break rompe todo el ciclo
else:
    print(f'''
    Fin Ciclo For
    
    Momento de probar la palabra continue
    en python

''')

for i in range(12):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')

