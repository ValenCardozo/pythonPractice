titulares = ["23 - Emiliano Martínez", "26 - Nahuel Molina", "13 - Cristian Romero", "19 - Nicolás Otamendi", "3 - Nicolás Tagliafico", "7 - Rodrigo De Paul", "14 - Enzo Fernández", "20 - Alexis Mac Allister", "11 - Ángel Di María", "10 - Lionel Messi", "9 - Julián Álvarez"]

titulares.append('DT - Lionel Scaloni')
titulares.insert(0, 'ARGENTINA')
print('La formacion de Argentina para la final del mundo es: ')
for titular in titulares:
    print(titular)

primerCambio = titulares.pop()
titulares.remove('3 - Nicolás Tagliafico')
del titulares[1:3]