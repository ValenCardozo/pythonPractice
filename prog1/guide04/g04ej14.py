# Pedir dos nombres y edades respectivas y luego construir una sola cadena con un texto que muestre el nombre del mayor y
# cuanto le lleva al menor. (Ejemplo:  entrada -> 'Juan' 30 'Pedro' 23 / salida -> 'Juan le lleva 7 años a Pedro')

limit = 2
names = []
ages = []

for i in range(2):
    name = input('Ingrese nombre: ')
    age = int(input('Ingrese edad: '))
    names.append(name)
    ages.append(age)

if ages[0] > ages[1]:
    takesTo = ages[0] - ages[1] 
    print(f'{names[0]} le lleva {takesTo} años a {names[1]}')
elif ages[1] > ages[0]:
    takesTo = ages[1] - ages[0] 
    print(f'{names[1]} le lleva {takesTo} años a {names[0]}')