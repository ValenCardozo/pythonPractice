# Escribe una función que cuente la cantidad de ocurrencias de una subcadena en una cadena de texto,
# permitiendo especificar si se debe realizar una búsqueda sin distinguir mayúsculas y minúsculas.

def countSubChar(subChar: str, text: str, strict: bool):
    count = 0
    index = 0
    if strict:
        text = text.lower()
        subChar = subChar.lower()

    while index < len(text):
        index = text.find(subChar, index)
        if index == -1:
            break
        count += 1
        index += len(subChar)

    return count

# text = 'Para ser campeón hay que ganarles a todos, campeón'
# find = 'campeón'
# response = countSubChar(find, text, True)
# print(response)

frase = 'Desde niña me encanta mirar la luna, por eso es que le puse de nombre Luna a mi hija'
print(countSubChar('luna', frase, True)) # 2
print(countSubChar('luna', frase, False))
