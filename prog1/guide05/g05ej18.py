# Hacer una función que determine si una cadena de texto contiene todas las vocales.

def allVocals(word: str):
    response = True
    vocals = ['a', 'e', 'i', 'o', 'u']

    for vocal in vocals:
        if word.find(vocal) == -1:
            response = False

    return response


print(allVocals('murciegalo'))