# Ejercicio 8
# Ingresar autos y sus precios y contar cuantos valen entre $3.460.000 y $12.850.000.
# Terminar la carga cuando el valor ingresado sea 0.

amount = 100
lowAmount = 3_460_000
highAmount = 12_850_000
rangeCars = 0

while amount != 0:
    carName = input('Ingrese modelo del auto: ')
    amount = int(input('Ingrese monto del vehiculo: '))

    if (amount > lowAmount and amount < highAmount):
        rangeCars = rangeCars + 1

print(f'La cantidad de autos en el rango de {lowAmount} y {highAmount} es {rangeCars}')
