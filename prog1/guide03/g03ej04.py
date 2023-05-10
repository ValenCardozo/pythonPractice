# Dada una lista con números, crear otra con los cuadrados de esos valores.

numbers = [2, 4, 6, 8]
squares = []

for number in numbers:
    square = number * number
    squares.append(square)

for i in range(len(squares)):
    print(f'El cuadrado del numero {numbers[i]} es {squares[i]}')