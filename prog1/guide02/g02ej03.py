# Ejercicio 3
# Pedir el ingreso de 5 números. Contar los mayores de 23. Mostrar el resultado.

limit = 23
count = 0
for i in range(5):
    number = int(input('Ingrese un numero: '))

    if (number > limit):
        count = count + 1

print(f'Usted ingreso {count} registros mayores a 23')
