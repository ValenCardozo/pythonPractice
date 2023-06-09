# Hacer una función que reciba una cadena de texto,y la recuadre del siguiente modo: ╔═══╗
# 186'║', 188'╝', 187'╗', 200'╚', 201'╔', 205'═'                                     ║ f ║ 
#                                                                                    ╚═══╝

def squareWord(word: str):
    square = ''
    for i in range(len(word) + 2):
        if i == 0:
            square += '╔'
        elif i == len(word) + 2 - 1:
            square += '╗'
        else:
            square += '═'

    square += '\n║'
    for i in range(len(word)):
        square += word[i]        
    square += '║\n'

    for i in range(len(word) + 2):
        if i == 0:
            square += '╚'
        elif i == len(word) + 2 - 1:
            square += '╝'
        else:
            square += '═'

    return square

word = input('Inserte una palabra: ')

print(squareWord(word))


