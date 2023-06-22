# inputStr: input de strings (validar largo por mínimo y/o máximo).

def inputStr(message: str, min: int=0, max: int=100):
    aprove = False
    # char = input(message)

    while aprove == False:
        char = input(message)
        try:
            if len(char) >= min and len(char) <= max:
                aprove = True
            else: 
                raise Exception()
        except:
            print(f'La cadena no cumple con un minimo de {min} y un maximo de {max} caracteres')
    
    return char


# password0 = inputStr('Password (entre 5 y 8 caracteres): ', 5, 8)
# password1 = inputStr('Password (al menos 4): ', 4)
# password2 = inputStr('Password (a lo sumo 5): ', max=5)
# password3 = inputStr('Password (sin rango): ')

# print(password0, password1, password2, password3)