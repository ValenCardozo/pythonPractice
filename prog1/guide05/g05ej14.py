# Crea una función que calcule la suma de los dígitos de un número entero.

def sumDigit(number: str):
    count = 0
    for digit in number:
        count += int(digit)

    return count

print(sumDigit('123'))