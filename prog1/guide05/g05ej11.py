# Cargar en listas los nombres y fechas de nacimiento de varias personas,
# luego recorrerlo y mostrar los nombres de los mayores de edad. Funciones de carga y cálculo de edad.

def loadNamesAndAges(limit: int):
    names = []
    ages = []
    for i in range(limit):
        name = input('Ingrese nombre: ')
        age = int(input('Ingrese edad: '))
        names.append(name)
        ages.append(age)

    return names, ages

def ofLegalAge(names: list, ages: list):
    legals = []
    for i in range(len(ages)):
        if ages[i] >= 18:
            legals.append(names[i])

    return legals

names, ages = loadNamesAndAges(3)
legalAge = ofLegalAge(names, ages)

print(f'Los mayores de edad son: {legalAge}')