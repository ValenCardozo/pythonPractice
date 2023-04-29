# Ejercicio 4
# Leer dos números y decir cuál es el mayor

firstNumber = int(input('Ingrese un numero: '))
secondNumber = int(input('Ingrese otro numero: '))

if firstNumber > secondNumber:
    print(firstNumber, 'es mayor a', secondNumber)
elif secondNumber > firstNumber:
    print(secondNumber, 'es mayor a', firstNumber)
else:
    print('son iguales')
