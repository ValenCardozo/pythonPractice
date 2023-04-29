# Ejercicio 13
# Ingresar la lluvia caída en milímetros para cada día de la semana.
# Mostrar al final el total de lluvia caída y la cantidad de días que no llovió.

weekDays = 7
rainedMilimeters = 0
rainedDays = 0

for i in range(weekDays):
    itsRaining = input(f'Llovio el dia {i + 1} de la semana? [si/no] ')

    if itsRaining == 'si':
        milimeters = int(input(f'Ingrese milimetros llovidos el dia {i + 1}: '))
        rainedDays = rainedDays + 1
        rainedMilimeters = rainedMilimeters + milimeters

nonRainedDays = weekDays - rainedDays

print(f'Durante la semana llovio un total de {rainedMilimeters}, teniendo {nonRainedDays} dias sin llover')
