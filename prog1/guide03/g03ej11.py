# Cargar en listas los nombres y fechas de nacimiento de varias personas,
# luego recorrerlo y mostrar los nombres de los mayores de edad.

names = []
birthdays = []
keepGoing = input('Desea ingresar registros? [si/no] ')

while keepGoing == 'si':
    name = input('Ingrese un nombre: ')
    date = float(input('Ingrese la fecha de su cumpleaños [año/mes/dia]:'))
    names.append(name)
    birthdays.append(date)
    keepGoing = input('Desea ingresar mas registros? [si/no] ')

today = input('Ingrese la fecha actual [año/mes/dia]: ')
