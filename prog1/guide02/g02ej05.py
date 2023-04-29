# Ejercicio 5
# Pedir los montos de sueldos de los empleados de una empresa hasta que no haya más y mostrar el total.

salaries = 0
keepGoing = 'si'
count = 1

while keepGoing == 'si':
    salary = float(input(f'Ingrese el salario del empleado #{count} '))
    salaries = salaries + salary
    count = count + 1

    keepGoing = input('Continuar ingresando? ')

print(f'El total de sueldos es {salaries}')