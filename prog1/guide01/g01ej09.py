# Ejercicio 9
# Realizar un algoritmo que permita ingresar un dato numérico y
# determinar si es un número positivo de dos dígitos.

number = int(input('Ingrese un numero: '))

if number >= 10:
    print('El numero', number, 'es positivo y de 2 digitos')
elif number >= 0:
    print('El numero', number, 'es positivo y tiene 1 digito')
else:
    print('El numero', number, 'es negativo')
