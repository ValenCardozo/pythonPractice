# Ejercicio 9
# Dada una serie de números reales positivos, determinar el valor máximo y mostrarlo al final.
# Se deberá ir preguntando si hay más números para ingresar.

keepGoing = 'si'
biggNumber = 0

while keepGoing == 'si':
    number = int(input('Ingrese un numero: '))
    if (number > biggNumber):
        biggNumber = number
    
    keepGoing = input('Desea ingresar mas numeros? ')

print(f'El numero mas grande los ingresados es {biggNumber}')

