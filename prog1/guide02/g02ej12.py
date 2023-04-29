# Ejercicio 12
# Pedir nombres y sexo de personas y mostrar el total de mujeres y el nombre de cada una
keepGoing = 'si'
womens = ''
countWomens = 0

while keepGoing == 'si':
    name = input('Ingrese el nombre: ')
    sex = input('Ingrese el sexo [m/f]: ')

    if sex == 'f':
        womens = womens + ', ' + name
        countWomens = countWomens + 1

    keepGoing = input('Desea continuar? [si/no]: ')

print(f'La cantidad de mujeres son {countWomens} y sus nombres son{womens}')
