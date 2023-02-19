def imprimir_Desc(numero):
    if numero < 0:
        print('Valor Incorrecto')
    elif numero == 0:
        return
    else:
        print(numero)
        imprimir_Desc(numero-1)

imprimir_Desc(5)
print('---------------------   - - -- - --- -')
imprimir_Desc(8)