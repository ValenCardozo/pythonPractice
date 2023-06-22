# Concatenar un número indeterminado de strings con un caracter específico (por defecto un espacio).


def concatenar(*args, conector=' '):
    text = ''
    for i in range(len(args)):
        if i == 0:
            text = args[i]
        elif i == len(args):
            text += args[i]
        else:
            text += conector + args[i]
    return text


print(concatenar('hola', 'pibe'))
print(concatenar('hola', 'pibe', conector='@'))
print(concatenar('techo', 'mesa', 'árbol', conector='###'))
print(concatenar('techo', 'mesa', 'árbol', conector='|||||||'))
