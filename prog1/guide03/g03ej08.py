# Cargar una lista con números.
# Invertir los elementos sin usar otra lista

list = []
keepGoing = ''

while keepGoing == '':
    number = int(input('Ingrese un numero: '))
    list.append(number)
    keepGoing = input('Desea ingresar mas numeros? [si/no] ')

limit = len(list) // 2
for i in range(limit):
    positionSwap = - (i + 1)
    swapElement = list[i]
    list[i] = list[positionSwap]
    list[positionSwap] = swapElement

print(list)
