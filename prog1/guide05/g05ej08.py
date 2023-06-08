# Ingresar nombres, luego buscar un nombre y de encontrarlo decir en qué posición está.

def loadNames(limit: list):
    names = []
    for i in range(limit):
        name = input('Ingrese nombre: ')
        names.append(name)

    return names

def findName(name: str, names: list):
    return names.index(name)

names = loadNames(3)
nameToFind = input('Nombre a buscar: ')
index = findName(nameToFind, names)

print(f'El nombre {nameToFind} esta en la posicion {index}')