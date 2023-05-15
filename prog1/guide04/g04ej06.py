# Quiero comer manzanas, solamente manzanas.
# Buscar una palabra completa en un texto y contar cuántas veces está.

text = 'Quiero comer manzanas, solamente manzanas.'
phraseSearch = input('Ingrese una palabra a buscar: ')
count = 0
index = 0

while index < len(text):
    index = text.find(phraseSearch, index)
    if index == -1:
        break
    count += 1
    index += len(phraseSearch)

print(f"La palabra '{phraseSearch}' aparece {count} veces en el texto {text}")
