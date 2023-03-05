class Producto:
    contador_productos = 0

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        self._id_order = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio

    @property
    def precio(self):
        return self._precio

    def __str__(self):
        return f'Producto: [ID: {self._id_order} NOMBRE: {self._nombre} PRECIO: {self._precio} ]'



if __name__ == '__main__':
    producto01 = Producto('Camisa', 300.00)
    producto02 = Producto('Pantalon', 250.00)
    producto03 = Producto('Gorra', 140.00)
    print(producto01)
    print(producto02)
    print(producto03)
