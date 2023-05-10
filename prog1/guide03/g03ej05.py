# Guardar en una lista los números pares mayores que 0 y menores que 31.

limit = 31
evenNumbers = []

for number in range(limit):
    if number != 0 and (number % 2) == 0:
        evenNumbers.append(number)

print(evenNumbers)
    