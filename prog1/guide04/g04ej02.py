# Transformar la cadena "Curso de Python" en la cadena "Curso de Programación en Python".
# Cortar la cadena original, agregarle el literal "Programación en" y concatenar.

phrase = 'Curso de Python'
addToPhrase = 'Programación en '
newPhrase = ''

for letter in phrase:
    if newPhrase == 'Curso de ':
        newPhrase += addToPhrase
    
    newPhrase += letter

print(newPhrase)