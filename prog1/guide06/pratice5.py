from functions import inputInt

persons = [
    "Vikki Tewkesbury,France,30-01-2000",
    "Virgie Brach,France,04-02-1994",
    "Adeline LaPadula,France,18-06-2002",
    "Willy Branscombe,Argentina,21-11-1997",
    "Diane Piffe,France,07-08-1993",
    "Britta Causbey,France,24-04-1991",
    "Elisabeth Cleeve,France,04-03-1991",
    "Rafael Ivanchenkov,France,28-04-2002",
    "Zerk Milsom,Norway,03-12-1994",
    "Adorne Ovington,United States,17-08-1991",
    "Kathryn Backshell,United States,04-03-1992",
    "Blake Colbeck,United States,18-01-1999",
    "Arron Bresnahan,United States,03-07-2001",
    "Deloria Dominguez,France,31-07-1990",
    "Grenville Aldersea,Argentina,11-01-2001",
    "Jemimah Haughian,Argentina,30-11-1998",
    "Con Gethen,United States,06-06-1992",
    "Roxie Igoe,France,31-03-2002",
    "Hollyanne Mottley,United States,05-01-1996",
    "Ambrosio Cadore,Norway,09-12-2002"
]

def inputChoice(options, question='Elija una opción'):
    question += ': '
    optionList = options.split('/')

    for i in range(len(optionList)):
        print(f'{i+1}) {optionList[i]}')
    op = inputInt(question, 1, len(optionList))
    return optionList[op-1]

def personsByCountry(findCountry, rows):
    countPersons = 0
    for row in rows:
        info = row.split(',')
        country = info[1]

        if country == findCountry:
            countPersons += 1

    return countPersons

def getBirthdayByLetter():
    return

country = 'Argentina'
howMany = personsByCountry(country, persons)
print(f'La cantidad de personas de {country} es {howMany}')

country = inputChoice('Germany/United States/Norway/France', 'Ingrese un pais')
howMany = personsByCountry(country, persons)
print(f'La cantidad de personas de {country} es {howMany}')

