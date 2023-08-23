# Hacer una clase Teléfono con los atributos:
# marca, modelo y costo mensual y un método que muestre (o devuelva) el costo anual.

class Phone:
    def __init__(self, brand, model, cost):
        self.brand = brand
        self.model = model
        self.cost = cost
    def getBrand(self):
        return self.brand
    def getModel(self):
        return self.model
    def getCostForMonth(self):
        return self.cost
    def getYearCost(self):
        return int(self.cost) * 12

celularcito = Phone('MOTOROLA', 'G2', '1000')
print(celularcito.getYearCost())