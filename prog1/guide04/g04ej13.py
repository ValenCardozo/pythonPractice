# Pedir el ingreso de un nombre completo en la forma <nombre> <apellido> (ejemplo: Juan Pérez)
# y mostrarlo invertido y con coma <apellido>,<nombre> (ejemplo: Perez, Juan).

identify = input('Ingrese nombre y apellido: ')
output = identify.split()

print(output[1] + ', ' + output[0])