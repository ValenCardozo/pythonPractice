# Ejercicio 4: Contar la cantidad de palabras.

def countWords(text):
    phrases = text.split()
    count = len(phrases)
    return count

text = 'Quiero comer manzanas, solamente manzanas'
letters = countWords(text)
print(f'La cantidad de palabras en el texto "{text}" son {letters}')
