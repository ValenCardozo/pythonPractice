# Ejercicio 10
# Dada una lista de nombres y de salarios respectivos, determinar el salario mínimo y mostrar el nombre de la persona que menos gana

lowestPaid = input('Ingrese un empleado: ')
lowerSalary = int(input('Ingrese su sueldo: '))
keepGoing = input('Desea ingresar mas empleados? ')

while keepGoing == 'si':
    employee = input('Ingrese un empleado: ')
    salary = int(input('Ingrese su sueldo: '))

    if (salary > lowerSalary):
        lowestPaid = employee
    
    keepGoing = input('Desea ingresar mas empleados? ')

print(f'El empleado que menos cobras es {employee}')