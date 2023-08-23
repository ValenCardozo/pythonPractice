# Definir una clase que al ser instanciada reciba un valor numérico y cargue una lista de nombres hasta esa cantidad.
# Hacer también un método que muestre la lista completa

class NamesCharger:
    def __init__(self, quantity):
        self.names = []
        for i in range(quantity):
            name = input('Ingrese un nombre: ')
            self.names.append(name)
    
    def showAllNames(self):
        for i in range(len(self.names)):
            print(self.names[i])

names = NamesCharger(4)
names.showAllNames()
