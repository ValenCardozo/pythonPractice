# Convierte una lista en cadena, solicitando al usuario el separador a utilizar. (Sin usar join)
list = ['quico', 123, 'mesa']
separator = input('Ingrese un separador: ')
text = ''

for i in range(len(list)):
    if i + 1 == len(list):
        text += format(list[i])
    else:
        text += format(list[i]) + separator

print(text)
