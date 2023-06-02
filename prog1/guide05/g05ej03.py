# Ejercicio 3: Contar la cantidad de letras (mayúsculas, minúsculas, acentuadas, eñes).

def countLetters(text):
    count = 0
    for caracter in text:
        isLetter = ord(caracter)
        if 65 <= isLetter <= 90 or 97 <= isLetter <= 122:
            count += 1
    return count

text = 'Quiero comer manzanas, solamente manzanas'
letters = countLetters(text)
print(f'La cantidad de letras en el texto "{text}" son {letters}')
