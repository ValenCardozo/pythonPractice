# Pedir el ingreso de 10 números.
# Contar los mayores de 23 y almacenar los que cumplen la condición.
# Mostrar la cantidad y los números guardados.

numbers = []
numbersQuantity = 10

for i in range(numbersQuantity):
    number = int(input('Ingrese un numero: '))

    if number > 23:
        numbers.append(number)

print(f'Se ingresaron {len(numbers)} numeros mayores a 23 y estos son {numbers}')


