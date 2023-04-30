# Cargar letras en una lista (while).
# Contar las vocales (for). Mostrar el total.

keepGoing = 'si'
letters = []
vowels = ['a', 'e', 'i', 'o', 'u']

while keepGoing == 'si':
    letter = input('Ingrese una letra: ')
    letters.append(letter)
    keepGoing = input('Desea continuar? [si/no]')

any(letter in letters for letter in vowels)
# for letter in letters:
#     any(letter in letters for letter in vowels)