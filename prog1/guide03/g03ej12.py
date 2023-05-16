# Pedir nombres y sexo de personas y mostrar al final el total de mujeres y el nombre de cada una.
keepGoing = 'si'
womens = ''
countWomens = 0
names = []
sexs = []

while keepGoing == 'si':
    name = input('Ingrese el nombre: ')
    sex = input('Ingrese el sexo [m/f]: ')
    names.append(name)
    sexs.append(sex)

    keepGoing = input('Desea continuar? [si/no]: ')

for i in range(len(names)):
    if sexs[i] == 'f':
        womens = womens + ', ' + names[i]

countWomens = sexs.count('f')


print(f'La cantidad de mujeres son {countWomens} y sus nombres son{womens}')
