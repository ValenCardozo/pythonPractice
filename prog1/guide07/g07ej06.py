#  Agregar al ejercicio 2 (clase Auto) un método que obtenga la antigüedad.
# En el programa principal mostrar cuáles autos tienen más de 5 años.

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def getBrand(self):
        return self.brand

    def getYear(self):
        return self.year

    def getAntiquity(self, actualYear):
        return int(actualYear) - int(self.year)

carList = []
carList.append(Car('BMW', '1998'))
carList.append(Car('FORD', '1997'))
actualYear = 2023

for car in carList:
    antiquity = car.getAntiquity(actualYear)
    if antiquity > 5:
        print(car.brand, antiquity)