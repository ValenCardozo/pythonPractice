# Definir una clase Persona cuyo constructor reciba nombre y edad.
# El programa principal pedirá en forma repetitiva (hasta que no haya más) los mismos datos,
# hará la instanciación de un objeto y lo agregará en una lista.
# Por lo tanto, los elementos de dicha lista serán objetos y podrá mostrarse con recorrido por elemento o por índices.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def insertPersons():
    persons = []
    keepGoing = 'si'
    while keepGoing == 'si':
        person = []
        name = input('Ingrese el nombre: ')
        age = input('Ingrese la edad: ')
        person = Person(name, age)

        persons.append(person)
        keepGoing = bool(input('Continuar?[si/no]: '))
    
    return persons

persons = insertPersons()
print(persons)