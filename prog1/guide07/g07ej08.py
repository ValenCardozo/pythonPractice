# Redefinir la clase auto con los atributos marca, modelo y año.
# Hacer una clase heredera TuAuto que agrega dueño y color.
# Hacer un método que devuelve el color y en el programa principal preguntar por un color y mostrar sólo los autos que cumplan esa condición.

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def getBrand(self):
        return self.brand

    def getYear(self):
        return self.year
    
    def getModel(self):
        return self.model

    def getAntiquity(self, actualYear):
        return int(actualYear) - int(self.year)

class YourCar(Car):
    def __init__(self, brand, model, year, owner, color):
        super().__init__(brand, model, year)
        self.owner = owner
        self.color = color
    
    def showBrand(self):
        print(f'Auto: {self.brand} Modelo: {self.model}')

    def getColor(self):
        return self.color

myCar = YourCar('BMW', '1998', 'e46', 'mio', 'azul')
color = 'azul'

if myCar.getColor() == color:
    myCar.showBrand()
# carList = []
# carList.append(Car('BMW', '1998', 'e46'))
# carList.append(Car('FORD', '1997', 'thunderbird'))
# actualYear = 2023

# for car in carList:
#     antiquity = car.getAntiquity(actualYear)
#     if antiquity > 5:
#         print(car.brand, antiquity)