# Definir una clase Telefono, sus atributos son: marca, modelo, sistema operativo, plan(costo) y cantidad de RAM.
# Sus métodos son: costo anual, mostrar Sistema Operativo y si es gama alta o no (con 6 o más gigas de RAM)

class Phone:
    def __init__(self, brand, model, oSystem, cost, ram):
        self.brand = brand
        self.model = model
        self.oSystem = oSystem
        self.cost = cost
        self.ram = ram
    
    def getYearCost(self):
        return int(self.cost) * 12

    def getOperatorSystem(self):
        return self.oSystem
    
    def isHighQuality(self):
        return int(self.ram) >= 6
    
    
smartPhone = Phone('MOTOROLA', 'G2', 'Android', 1000, 8)

print(smartPhone.getYearCost())
print(smartPhone.getOperatorSystem())
if smartPhone.isHighQuality():
    print('Es de calidad alta')
else:       
    print('Es de calidad media/baja')