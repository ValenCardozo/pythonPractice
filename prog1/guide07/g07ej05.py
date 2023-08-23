# Hacer una clase Persona con dos métodos:
# uno para saber si es mayor de edad y el otro para determinar si es varón o mujer.
# En el programa principal instanciarlo, tomar nombre, edad y sexo,
# y finalmente mostrar un cartel que diga por ejemplo ‘Juan es mayor de edad y es varón’

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def isAdult(self):
        if self.age >= 18:
            return 'es mayor de edad'
        else:
            return 'no es mayor de edad'

    def getGender(self):
        return self.gender
    
person = Person('maria', 18, 'mujer')

print(f'{person.name} {person.isAdult()} y es {person.gender}')