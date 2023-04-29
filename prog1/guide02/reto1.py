# Reto 1 
# Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión),
# sustituyendo los siguientes:
# Múltiplos de 3 por la palabra "fizz".
# Múltiplos de 5 por la palabra "buzz".
# Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
# 	Sugerencia: Usar el operador % que devuelve el resto de una división.
# 	Nota: Un número es múltiplo de otro si lo contiene un número entero de veces.
# 	Salida esperada: 1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz 16 17 fizz 19 buzz

totalNumbers = 100
for i in range(totalNumbers):
    multipleOfThree = i % 3
    multipleOfFive = i % 5
    if multipleOfThree == 0 and multipleOfFive == 0:
        print('fizzbuzz \n')
    elif multipleOfThree == 0:
        print('fizz \n')
    elif multipleOfFive == 0:
        print('buzz \n')
    else:
        print(f'{i} \n')

