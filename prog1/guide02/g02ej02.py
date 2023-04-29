# Ejercicio 2
# Preguntar si hay datos para ingresar,
# en caso afirmativo solicitar un número entero y
# decir si es negativo o no. Preguntar si repite.

moreNumbers = ''
while moreNumbers != 'no':
    existInfo = input('Hay datos para ingresar? ')

    if (existInfo == 'si'):
        number = int(input('Ingrese un numero: '))

        if (number >= 0):
            print(f'El numero {number} es positivo')
        else:
            print(f'El numero {number} es negativo')
        
        moreNumbers = input('Desea continuar? ')
    else:
        moreNumbers = 'no'
    
