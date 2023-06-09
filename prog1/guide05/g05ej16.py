# Implementa una función que determine si una cadena de texto contiene solo caracteres numéricos (es decir, si es un entero).

def onlyNumbers(text: str):
    isNumber = True
    for caracter in text:
        if ord(caracter) < 48 or ord(caracter) > 57:
            isNumber = False

    return isNumber

print(onlyNumbers('123145ko'))
