# Ejercicio 2: Buscar una palabra y reemplazarla por otra todas las veces que aparezca.
# Ej.: ‘peras’ en lugar de ‘manzanas’ quedaría 'Quiero comer peras, solamente peras.'

def replaceWord(word, text):
    index = 0
    while 'manzanas' in text:
        index = text.find('manzanas')
        text = text[0:index] + word + text[index + len('manzanas'):]
    return text

word = 'conchas'
text = 'Quiero comer manzanas, solamente manzanas'

print(replaceWord(word, text))