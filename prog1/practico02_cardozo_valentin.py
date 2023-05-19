persons = [
    "Josefa Taponales,France(Europe),30-01-2000",
    "Virgie Brach,Argentina(America),04-02-1994",
    "Adeline Quispe,United States(America),18-06-2002",
    "Willy Branscombe,Norway(Europe),21-11-2007",
    "Diane Piffe,France(Europe),07-08-1993",
    "Britta Causbey,Germany(Europe),24-01-2000",
    "Elisabeth Cleeve,Norway(Europe),04-03-1991",
    "Sasha Ivanchenkov,Argentina(America),28-04-2002",
    "Zerk Milsom,Norway(Europe),03-12-1994",
    "Kathryn Backshell,United States(America),04-01-2000"
]


# Ejercicio 1
year = int(input('Ingrese año: '))

for person in persons:
    data = person.split(',')
    birthYear = int(data[2][6:])
    if birthYear < year:
        lastName = (data[0].split())[1]
        print(lastName)

# Ejercicio 2
country = input('Ingrese pais: ')
count = 0

for person in persons:
    data = person.split(',')
    countryPerson = data[1][:data[1].find('(')]
    if countryPerson == country:
        count += 1

print(f'La cantidad de personas de {country} es {count}')


# Ejercicio 3
europeanYoung = ''
yearYoung = 0

for person in persons:
    data = person.split(',')
    statePerson = data[1][data[1].find('(')+1:-1]
    if statePerson == 'Europe':
        birthYear = int(data[2][6:])
        
        if birthYear > yearYoung:
            yearYoung = birthYear
            europeanYoung = (data[0].split())[0]

print(f'La persona mas joven de Europe es {europeanYoung}')
        






