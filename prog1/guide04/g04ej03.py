# Decir cuántas veces se repite una letra cualquiera, en un texto dado.
# Por recorrido.

text = 'Me gusta la milanesa, como me gusta la milanesa'
countLetter = input('Ingrese una letra para buscar: ')
appearsLetter = 0

for letter in text:
    if letter == countLetter:
        appearsLetter += 1

print(f'La letra {countLetter} aparece {appearsLetter} veces en el texto {text}')