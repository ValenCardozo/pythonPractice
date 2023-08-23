# Definir una clase Auto con un método que le permita poner la marca y el año.
# En el programa principal declarar dos instancias (objetos), cargarlas y mostrar las marcas de los dos autos

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def getBrand(self):
        return self.brand
    def getYear(self):
        return self.year

firstCar = Car('BMW', '1998')
secondCar = Car('FORD', '1997')

print(firstCar.brand)
print(secondCar.brand)