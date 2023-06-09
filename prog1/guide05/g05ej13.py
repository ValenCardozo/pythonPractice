# Hacer una función que dibuje una raya con un caracter y una longitud dada.

def askCaracterAndLength():
    caracter = input('Ingrese un caracter: ')
    length = int(input('Ingrese longuitud de la linea: '))

    return caracter, length

def paintLineWithCaracter(caracter: str, length: int):
    line = ''
    for i in range(length):
        line = line + caracter

    return line

caracter, length = askCaracterAndLength()
line = paintLineWithCaracter(caracter, length) 
print(line)
