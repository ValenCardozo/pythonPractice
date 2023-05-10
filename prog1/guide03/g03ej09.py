# Cargar en dos listas paralelas nombres y sueldos.
# Luego mostrar los nombres de las personas que ganan más de $185000.

names = []
salaries = []
peopleAboveAverage = []
averageSalary = 185000
keepGoing = input('Desea ingresar registros? [si/no] ')

while keepGoing == 'si':
    name = input('Ingrese un nombre: ')
    salary = float(input('Ingrese su sueldo: '))
    names.append(name)
    salaries.append(salary)
    keepGoing = input('Desea ingresar mas registros? [si/no] ')

for i in range(len(salaries)):
    if (salaries[i] > averageSalary):
        peopleAboveAverage.append(names[i])

print(f'Las persona que cobran mas de {averageSalary} son {peopleAboveAverage}')
