# Ejercicio 5
# Leer dos números reales y mostrarlos en orden creciente.

firstNumber = int(input('Ingrese un numero: '))
secondNumber = int(input('Ingrese otro numero: '))

if firstNumber > secondNumber:
    print(secondNumber, firstNumber)
elif secondNumber > firstNumber:
    print(firstNumber, secondNumber)
else:
    print('son iguales')
