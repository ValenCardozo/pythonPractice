# Ejercicio 6: Definir una lista de 10 posiciones con letras. Contar las vocales y mostrar el total.

def countVocal(letters):
    vocals = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for vocal in vocals:
        for caracter in letters:
            if caracter == vocal:
                count += 1
    
    return count

letters = ['a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u']
vocals = countVocal(letters)
print(f'La cantidad de vocales en la lista es {vocals}')