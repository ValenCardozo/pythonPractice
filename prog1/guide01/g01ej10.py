# Ejercicio 10
# Preguntar nombre, carrera en la que se inscribe y
# ciudad donde vive un ingresante al Instituto.
# Los estudiantes de la carrera de Electromecánica y
# que no viven en Río Cuarto tendrán un 15% de descuento
# en la cuota que es de $7000.
# Mostrar nombre, ciudad, carrera y monto final de la cuota.

# name = input('Ingrese nombre: ')
# city = input('Ingrese ciudad donde vive: ')
# career = input('Ingrese carrera a la que pertenece: ')
# amount = 7000

# if career == 'Electromecanica' and city == 'Rio Cuarto':
#     discount = 0.15 * amount
#     finallyAmount = amount - discount
# else:
#     finallyAmount = amount

# print(f"nombre: {name}, ciudad: {city}, carrera: {career}, monto: ${finallyAmount}")

# --- Modificado para utilizar ciclo for

numberStudents = int(input('Cantidad de alumnos a ingresar: '))

for i in range(numberStudents):
    print(f'Estudiante # {i + 1}')
    name = input('Ingrese nombre: ')
    city = input('Ingrese ciudad donde vive: ')
    career = input('Ingrese carrera a la que pertenece: ')
    amount = 7000

    if career == 'Electromecanica' and city == 'Rio Cuarto':
        discount = 0.15 * amount
        finallyAmount = amount - discount
    else:
        finallyAmount = amount

    print(f"nombre: {name}, ciudad: {city}, carrera: {career}, monto: ${finallyAmount}")
    


