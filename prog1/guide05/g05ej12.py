# Pedir el ingreso de un nombre completo (Juan Pérez) y mostrarlo invertido y con coma (Pérez, Juan).

def askName():
    return input('Ingrese nombre y apellido: ')

def reverseName(name: str):
    reverse = ''
    if name != '':
        info = name.split()
        reverse = info[1] + ', ' + info[0]
    
    return reverse

name = askName()
reversedName = reverseName(name)

print(reversedName)