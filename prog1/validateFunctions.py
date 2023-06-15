# Ejercicio 1 con validaciones
# Pedir dos números enteros, sumarlos y mostrar el resultado.
# import sys
# sys.path.insert(1, '/home/user/Documents/ITEC/Progamacion I/pythonPractice/prog1/')

from libraries.functions import inputInteger
# def inputInteger(message: str, insult: str):
#     validate = False
#     while not validate:
#         number = input(message)
#         try:
#             number = int(number)
#             validate = True
#         except:
#             print(insult)

#     return number

firstNumber = inputInteger('Ingrese un entero: ', 'An integer, ape!')
secondNumber = inputInteger('Ingrese otro entero: ', 'Is very dificult, monkey?')

suma = firstNumber + secondNumber

print('La suma es', suma)

