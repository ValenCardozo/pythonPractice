# Heredar de la clase Auto una clase Marca, que agregue el atributo Modelo.
# Instanciar en  el programa principal (una sola línea en total).
# La salida debe ser por ejemplo: Auto: VW Modelo: Gol

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def getBrand(self):
        return self.brand

    def getYear(self):
        return self.year
    
    def getModel(self):
        return self.model

    def getAntiquity(self, actualYear):
        return int(actualYear) - int(self.year)

class Model(Car):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model
    
    def showBrand(self):
        print(f'Auto: {self.brand} Modelo: {self.model}')

car = Model('BMW', '1998', 'e46')
car.showBrand()