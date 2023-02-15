print('Proporcione los siguientes datos del libro: ')
nombre = input('Proporciona el nombre: ')
id = int(input('Proporciona el id: '))
precio = float(input('Proporciona el precio: '))
envio = input('Indica si el envio es gratuito (True / False): ')

if envio == 'True':
    envio = True
elif envio == 'False':
    envio = False
else:
    envio = 'Valor Incorrecto, debe ser ( True / False )'

print(f'''
    Nombre: {nombre}
    Id: {id}
    Precio: {precio}
    Envio Gratuito?: {envio}
''')

