# Eliminar el plural en esta frase: “Real Madrid gana las copas.”
# Recorrer y quitar las eses. Sugerencia: Usar otra string.

phrase = 'Real Madrid gana las copas.'
newPhrase = ''

for letter in phrase:
    newLetter = letter

    if letter == 's':
        newLetter = ''
    
    newPhrase = newPhrase + newLetter
    print(newPhrase)

print(newPhrase)
    
