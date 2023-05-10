# Primer for: Almacenar en dos listas paralelas, nombres y sexos de 8 personas. 
# Segundo for: Recorrerlas y guardar los nombres de las mujeres en una nueva lista. 
# Mostrar los elementos de la lista resultante.

names = []
genders = []
women = []
limit = 8

for i in range(limit):
    name = input('Ingrese un nombre: ')
    gender = input('Ingrese su sexo: ')
    names.append(name)
    genders.append(gender)

for j in range(len(genders)):
    if (genders[j] == 'F'):
        women.append(names[j])

print(f'Las mujeres de la lista son {women}')
