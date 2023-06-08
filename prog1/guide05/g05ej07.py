# Almacenar en dos listas paralelas, nombres y sexos de 8 personas.
# Al finalizar, recorrerlas y mostrar los nombres de las mujeres.
# Dos funciones: carga y mostrarMujeres

def loadNamesAndSexs(limit):
    names = []
    sexs = []
    for i in range(limit):
        name = input('Ingrese nombre: ')
        sex = input('Ingrese sexo: ')
        names.append(name)
        sexs.append(sex)

    return names, sexs

def showWomens(names: list, sexs: list):
    womens = []
    for i in range(len(sexs)):
        if sexs[i] == 'f':
            womens.append(names[i])

    return womens

names, sexs = loadNamesAndSexs(3)
womens = showWomens(names, sexs)

print(f'Las mujeres son: {womens}')

