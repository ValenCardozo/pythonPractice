# Contar la cantidad de letras (no incluir los separadores).
# Resolver con ASCII para hacerlo general
# Mayusculas de 65 a 90, minusculas de 97 a 122

text = 'Quiero comer manzanas, solamente manzanas.'
count = 0

for caracter in text:
    isLetter = ord(caracter)
    if 65 <= isLetter <= 90 or 97 <= isLetter <= 122:
        count += 1

print(count)