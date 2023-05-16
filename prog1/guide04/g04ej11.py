# Averiguar qué cantidad de letras tiene la palabra más larga y cual es

text = 'Quiero comer manzanas, solamente manzanas.'

phrases = text.split()
count = len(phrases)
longPhrase = ''

for phrase in phrases:
    if phrase.find('.'):
        phrase = phrase.replace('.', '')

    if phrase.find(','):
        phrase = phrase.replace(',', '')

    if len(phrase) > len(longPhrase):
        longPhrase = phrase

print(f'El texto contiene {count} palabras, y la mas larga es {longPhrase}')