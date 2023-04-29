# Ejercicio 7
# Pedir un nombre y una opción ('>' o '<') y
# según esta mostrar por ejemplo.: Juan es menor de edad

name = input('Ingrese un nombre: ')
age = input('Ingrese si es mayor o menor, > o <: ')

if age == '<':
    print(name, 'es menor de edad')
elif age == '>':
    print(name, 'es mayor de edad')
