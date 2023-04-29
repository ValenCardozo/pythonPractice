# Dada una lista de numeros:
# 1- Obtener el promedio.
# 2- Obtener los valores mayores al promedio.

numberList = [3, 4, 5, 6, 18, 9, -2, 4]
mayorToAverage = []
numbersSum = 0

for number in numberList:
    numbersSum += number

average = numbersSum // len(numberList)

for number in numberList:
    if number > average:
        mayorToAverage.append(number)

print(f'Lista de numeros {numberList}')
print(f'Promedio {average}')
print(f'Mayores al promiedos {mayorToAverage}')