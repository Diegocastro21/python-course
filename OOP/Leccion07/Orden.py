from Producto import Producto
class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._productos = list(productos)

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total
    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str +=  '\n' + producto.__str__()

        return f'Orden: {self._id_orden}, {productos_str}'

if __name__ == '__main__':
    producto01 = Producto('Camisa', 300.00)
    producto02 = Producto('Pantalon', 250.00)
    producto03 = Producto('Gorra', 140.00)
    producto04 = Producto('Correa', 40.00)

    productos = [producto01, producto02, producto03]
    orden1 = Orden(productos)
    print(orden1)
    print(f'Total Orden {orden1._id_orden}: {orden1.calcular_total()}')
    productos.append(producto04)
    orden2 = Orden(productos)
    print(orden2)
    print(f'Total Orden {orden2._id_orden}: {orden2.calcular_total()}')