# Dados estos datos desordenados, encontrar los sueldos y obtener el total.
text = 'Pedro$120.000, Ana(frontend)$512.700, el portero$175.120, el pibe del backend(capaz hay que actualizarle!)$371.459, revisar bien el total de erogaciones!'
phrases = text.split('$')
total = 0

for phrase in phrases:
    number = ''
    for letter in phrase:
        if letter.isdigit():
            number += letter
    if number != '': 
        total = total + int(number)

print(total)