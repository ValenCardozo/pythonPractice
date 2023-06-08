# Dada una lista cargada con números enteros, obtener el promedio de ellos.
# Mostrar por pantalla dicho promedio y los números ingresados que sean mayores que él.
# Dos funciones: promedio y mayorQue

def average(numbers: list):
    total = 0
    for number in numbers:
        total += number
    
    return total / len(numbers)

def higherThanAverage(average: float, numbers: list):
    highers = []
    for number in numbers:
        if number > average:
            highers.append(number)
    
    return highers

numbers = [2, 4, 6, 7, 1, 9]
medium = average(numbers)
mayors = higherThanAverage(medium, numbers)

print(f'Los numeros mayores al promedio {medium} son {mayors}')