calificacion = float(input('Proporciona un valor entre 0 y 10: '))
nota = None
if 9 <= calificacion <= 10:
    print('A')
elif 8 <= calificacion <= 9:
    print('B')
elif 7 <= calificacion <= 8:
    print('C')
elif 6 <= calificacion <= 7:
    print('D')
elif 5 <= calificacion <= 6:
    print('F')
else:
    nota = 'Valor Incorrecto.'

