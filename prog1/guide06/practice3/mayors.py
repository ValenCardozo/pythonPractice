# Tengo un archivo de texto personas.txt, con los nombres y
# fechas de nacimiento de varias personas.
# Quiero obtener un nuevo archivo de texto, de nombre mayores.txt,
# donde guardaremos los nombres y las edades de las personas mayores de edad.

from agesFunctions import calculateAge, ofLegalAge

with open('practice3/persons.txt') as persons:
    personsData = persons.readlines()

legals = ['Nombre, Edad\n']
for i in range(1,len(personsData)):
    person = personsData[i]
    personData = person.split(', ')
    
    name = personData[0]
    birthday = personData[1]

    birthday.strip('\n')
    birthdayInfo = birthday.split('/')
    age = calculateAge(birthdayInfo[0], birthdayInfo[1], birthdayInfo[2])
    if age > 18:
        legals.append(f'{name}, {str(age)}\n')

with open('practice3/mayors.txt', 'w') as mayors:
    mayors.writelines(legals)