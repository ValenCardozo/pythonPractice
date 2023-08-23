# Usando inputStr(la función realizada en el ejercicio anterior),
# escribir una función que valide un nombre de usuario, agregando restricciones específicas,
# como por ejemplo que tenga al menos 8 caracteres en total, al menos una letra,
# al menos 1 dígito numérico y al menos 1 caracter especial entre estos: #, $, %,&.

from g06ej04 import inputStr

def inputUser(message: str):
    min = 0
    max = 8
    caracters = ['#', '$', "%", '&']
    inputPassword = True

    while inputPassword:
        try:
            password = inputStr(message, min, max)
            if not containsSpecialCharacters(password, caracters):
                raise Exception(f'{password} not contains this caracters {caracters}')

            if not containNumbers(password):
                raise Exception(f'{password} not contains any number')

            inputPassword = False
        except Exception as error:
            print(f"An exception occurred: {str(error)}")

    return password

def containNumbers(text: str):
    containNumber = False
    for char in text:
        if ord(char) >= 48 and ord(char) <= 57:
            containNumber = True

    return containNumber

def containsSpecialCharacters(text: str, characters: list):
    specialChars = False
    for caracter in characters:
            if caracter in text:
                specialChars = True

    return specialChars

usuario = inputUser('Ingrese un nombre de usuario válido (debe contener como mínimo una letra, un dígito y al menos uno de estos caracteres especiales:  #, $, %,&): ')
print(usuario)