# Pasar una palabra a mayúsculas cambiando los caracteres uno por uno usando la tabla ASCII
# de referencia (googlear la tabla y las funciones de conversión en Python).

toUpper = 32
phrase = input('Ingrese una palabra en minuscula: ')
lowPhrase = ''

for letter in phrase:
    lowLetter = ord(letter)
    lowLetter = chr(lowLetter - toUpper)
    lowPhrase += lowLetter

print(lowPhrase)