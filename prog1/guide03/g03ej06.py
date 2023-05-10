# Ingresar nombres en una lista, luego buscar un nombre y de encontrarlo decir en qué posición está

names = []
keepGoing = 'si'

while keepGoing == 'si':
    name = input('Ingrese un nombre: ')
    names.append(name)
    keepGoing = input('Desea continuar? [si/no] ')

searchName = input('Desea buscar un nombre? [si/no] ')
while searchName == 'si':
    watName = input('Ingrese el nombre a buscar: ')
    for name in names:
        if name == watName:
            index = name.index(watName)
            print(f'El nombre {watName} se encuentra en la posicion {index}')
    
    searchName = input('Desea buscar otro nombre? [si/no] ')


