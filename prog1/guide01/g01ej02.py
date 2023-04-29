# Ejercicio 2
# Pedir tres notas, calcular el promedio y mostrarlo.

firstNote = float(input('Ingrese la primer nota '))
secondNote = float(input('Ingrese la segunda nota '))
thirdNote = float(input('Ingrese la tercer nota '))

average = (firstNote + secondNote + thirdNote) / 3

print('El promedio de las notas', firstNote, secondNote, thirdNote, 'es', round(average, 2))