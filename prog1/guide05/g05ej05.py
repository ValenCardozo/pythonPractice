# Ejercicio 5: Averiguar qué cantidad de letras tiene la palabra más larga. 
# Para ello, primero cargar cada palabra en una lista y luego obtener la solicitada. Usar dos funciones

def longWord(text):
    words = text.split()
    longWord = ''

    for word in words:
        if word.find('.'):
            word = word.replace('.', '')

        if word.find(','):
            word = word.replace(',', '')

        if len(word) > len(longWord):
            longWord = word

    return longWord

def countLetters(word):
    count = 0
    for caracter in word:
        isLetter = ord(caracter)
        if 65 <= isLetter <= 90 or 97 <= isLetter <= 122:
            count += 1
    return count

text = 'Quiero comer manzanas, solamente manzanas'
word = longWord(text)
letters = countLetters(word)

print(f'La palabra mas larga del texto "{text}" es "{word}" y tiene {letters} letras')



