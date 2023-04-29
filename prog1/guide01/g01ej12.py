# Ejercio 12
# Calcular el sueldo a cobrar teniendo en cuenta que
# los empleados que no han faltado y cuya antigüedad es superior a 5 años,
# tienen un adicional del 30% sobre el sueldo básico ($47.000).
# Pedir la cantidad de días no trabajados y año de ingreso en la empresa.

# daysDontWork = int(input('Ingrese dias sin trabajar: '))
# entryYear = int(input('Ingrese año de ingreso: '))
# salary = 47000
# extra = 0.30 * salary
# actuallyYear = 2023
# salaryToPay = salary

# if daysDontWork == 0 and (actuallyYear - entryYear) > 5:
#     salaryToPay = salary + extra

# print('El salario a cobrar es:', salaryToPay)

# ----- Modificado con ciclos
employees = 3
for i in range(employees):
    employeeName = input('Ingrese nombre del empleado a pagar: ')
    daysDontWork = int(input('Ingrese dias sin trabajar: '))
    entryYear = int(input('Ingrese año de ingreso: '))
    salary = 47000
    extra = 0.30 * salary
    actuallyYear = 2023
    salaryToPay = salary

    if daysDontWork == 0 and (actuallyYear - entryYear) > 5:
        salaryToPay = salary + extra

    print(f'El salario a cobrar del empleado {employeeName} es: {salaryToPay}')