# Recibir por teclado una cadena de números e insertar un punto cada 3 dígitos como divisorio de miles.
# Ej. 1234567890 debería devolver 1.234.567.890

# number = input('Ingresa un numero gorriado')
number = '1234567890'
newNumber = ''
count = -1

for caracter in reversed(number):
    if count == 2:
        newNumber = caracter + '.' + newNumber
        count = 0
    else:
        newNumber = caracter + newNumber
        count += 1

print(newNumber)