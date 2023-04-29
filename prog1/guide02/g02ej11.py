# Ejercicio 11
# Ingresar 7 números enteros y en el caso de que sean naturales de una sola cifra mostrar un cartel por cada uno.

howNumbers = 7

for i in range(howNumbers):
    number = int(input(f'#{i + 1} Ingrese un numero: '))
    if number < 10 and number > 0:
        print(f'El numero {number} es natural')