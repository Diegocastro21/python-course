class Person:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Person: [Nombre: {self.nombre}, Edad: {self.edad}]'

class Employee(Person):
    def __init__(self, nombre, edad, salary):
        super().__init__(nombre, edad)
        self.salary = salary

    def __str__(self):
        return f'Employee: [{super().__str__()}, Salary: {self.salary}]'

if __name__ == '__main__':
    employee = Employee('Fulanito de tal', 19, 32000.0)
    print(f'{employee.nombre} {employee.edad} {employee.salary}')