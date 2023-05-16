# Mostrar el valor doble del número de dos cifras (que es el único número) encontrado en la cadena.
# Ej.: 'Juan tiene 25 años' mostraría el número 50, ‘El dólar va a llegar este mes a 500 pesos casi seguro’,  mostraría 1000

text = 'Juan tiene 25 años'
phrases = text.split()

for phrase in phrases:
    if phrase.isdigit():
        digit = int(phrase)

doble = digit * 2

print(f'El doble del numero encontrado es {doble}')
