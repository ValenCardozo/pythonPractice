# Ejercicio 11
# El costo del pasaje a Córdoba es de $2000.
# La empresa realiza un descuento de un 40 %
# sobre el costo del boleto a los niños que tienen entre 5 y 10 años y
# a los jubilados (mayores de 65).
# Pedir nombre y edad y mostrar el nombre y el valor final del pasaje.

# name = input('Ingrese nombre: ')
# age = int(input('Ingrese edad: '))
# amount = 2000

# if (age >= 5 and age <= 10) or age > 65:
#     discount = 0.40 * amount
#     finallyAmount = amount - discount
# else:
#     finallyAmount = amount

# print(f"nombre: {name}, monto: ${finallyAmount}")

# --- Modificado para realizarlo con while

morePassengers = 'si'
while morePassengers == 'si':
    name = input('Ingrese nombre: ')
    age = int(input('Ingrese edad: '))
    amount = 2000

    if (age >= 5 and age <= 10) or age > 65:
        discount = 0.40 * amount
        finallyAmount = amount - discount
    else:
        finallyAmount = amount

    print(f"nombre: {name}, monto: ${finallyAmount}")

    morePassengers = input('Hay mas pasajeros? ')

print('Gracias vuelva prontos')