# Ejercicio 6
# Preguntar cuántas personas se van a cargar y luego solicitar sus edades, mostrando al final la edad promedio.

howMany = int(input('Cuantas personas desea ingresar? '))
ages = 0
for i in range(howMany):
    age = int(input(f'Ingrese la edad de la persona {i + 1} '))
    ages = ages + age

ageAverages = round(ages / howMany)
print(f'La edad promedio de las personas ingresadas es {ageAverages}')