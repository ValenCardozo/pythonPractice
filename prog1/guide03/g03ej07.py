# Eliminar todos los valores iguales de una lista.
# Previamente, solicitar el valor y si no está, mostrar un cartel diciendo que no lo ha encontrado

numbers = []
keepGoing = 'si'

while keepGoing == 'si':
    number = int(input('Ingrese un numero: '))
    numbers.append(numbers)
    keepGoing = input('Desea ingresar mas numeros? [si/no] ')

searchNumber = input('Desea buscar un numero? [si/no] ')
while searchNumber == 'si':
    watNumber = int(input('Ingrese el numero a buscar: '))
    found = False
    for i in range(len(numbers)):
        if numbers[i] == watNumber:
            numbers.remove(watNumber)
            found = True
    
    if not found:
        print(f'No se encontro el valor de {watNumber}')
            
    searchNumber = input('Desea buscar otro numero? [si/no] ')