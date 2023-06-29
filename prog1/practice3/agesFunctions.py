import datetime

def loadNamesAndAges(limit: int):
    names = []
    ages = []
    for i in range(limit):
        name = input('Ingrese nombre: ')
        age = int(input('Ingrese edad: '))
        names.append(name)
        ages.append(age)

    return names, ages

def ofLegalAge(names: list, ages: list):
    legals = []
    for i in range(len(ages)):
        if ages[i] >= 18:
            legals.append(names[i])

    return legals

def calculateAge(day, month, year):
    now = datetime.datetime.now()

    age = int(now.strftime('%Y')) - int(year)
    if month > now.strftime('%m'):
        age += 1
    elif month == now.strftime('%m'):
        if day > now.strftime('%d'):
            age += 1
        elif day == now.strftime('%d'):
            age += 1
    
    return age


    print(age)
