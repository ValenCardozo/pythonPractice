# Ingresar la lluvia caída en milímetros para cada día de la semana.
# Mostrar al final el total de lluvia caída y el nombre del día que más llovió.

week = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
totalRainFall = 0
rainiestDay = week[0]
maxRainFall = 0

for i in range(len(week)):
    howRainFall = float(input(f'Ingrese la cantidad de lluvia caida en el dia {week[i]}: '))
    totalRainFall += howRainFall

    if howRainFall > maxRainFall:
        rainiestDay = week[i]

print(f'El dia que mas llovio fue {rainiestDay} y la cantidad llovida en la semana fue {totalRainFall}')