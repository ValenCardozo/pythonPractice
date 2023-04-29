# Ejecicio 1
# Mostrar por pantalla una lista de 10 números enteros consecutivos,
# comenzando con un número ingresado por teclado.

consecNumbers = 11
startNumber = int(input('Ingrese un numero: '))

for i in range(consecNumbers):
    print(startNumber + i)
