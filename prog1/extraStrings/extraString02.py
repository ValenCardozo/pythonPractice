# Dadas dos listas con nombres, una de varones y otra de mujeres, solicitar una letra inicial 
# y mostrar los nombres que comiencen con ella en ambas listas en una string concatenada con guiones.

keepGoing = 'si'
names = []
sexs = []
womens = []
mens = []

while keepGoing == 'si':
    women = input('Ingrese el nombre de mujer: ')
    men = input('Ingrese el nombre de hombre: ')
    womens.append(women)
    mens.append(men)

    keepGoing = input('Desea continuar? [si/no]: ')

letter = input('Ingrese una inicial: ')
findNames = []

for women in womens:
    if women.find(letter) != -1:
        findNames.append(women)
        
for men in mens:
    if men.find(letter) != -1:
        findNames.append(men)

print('-'.join(findNames))