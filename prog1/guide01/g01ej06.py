# Ejercicio 6
# Leer dos números y luego una opción (puede ser '+' o '-'),
# y según la opción elegida realizar el cálculo.

firstNumber = int(input('Ingrese un numero: '))
secondNumber = int(input('Ingrese otro numero: '))
option = input('Ingrese operacion a realizar, + o -: ')

if option == '+':
    print('La suma de los numeros es', firstNumber + secondNumber)
elif option == '-':
    print('La resta de los numeros es', firstNumber - secondNumber)
