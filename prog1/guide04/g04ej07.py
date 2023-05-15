# Buscar una palabra y reemplazarla por otra todas las veces que aparezca.
# Ej.: ‘peras’ en lugar de ‘manzanas’ quedaría 'Quiero comer peras, solamente peras.'
# Sin usar replace.

text = 'Quiero comer manzanas, solamente manzanas.'
phraseChange = 'peras'
newPhrase = text

index = 0
notFound = -1
while 'manzanas' in newPhrase:
    index = newPhrase.find('manzanas')
    newPhrase = newPhrase[0:index] + phraseChange + newPhrase[index + len('manzanas'):]

print(newPhrase)
