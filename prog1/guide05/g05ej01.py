#Ejercicio 1: Cuántas veces se repite una letra cualquiera

def countLetter(findLetter, string):
    count = 0
    index = 0

    while index < len(string):
        index = text.find(findLetter, index)
        if index == -1:
            break
        count += 1
        index += len(findLetter)
    return count

word = 'manzanas'
text = 'Quiero comer manzanas, solamente manzanas'
repeat = countLetter(word, text)
print(f'La palabra {word} se repite {repeat} veces en el texto "{text}"')