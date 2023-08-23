born2008="Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"
born2018= "Liam,19837,m,Emma,18688,f,Noah,18267,m,Olivia,17921,f,Michael,14516,m,Ava,14924,f,James,13525,m,Isabella,14464,f,Oliver,13389,m,Sophia,13928,f"

def formatNames(nameString: str):
    names = {
        'female': [],
        'male': []
    }

    array = nameString.split(',')
    for i in range(0, len(array), 3):
        name = array[i]
        quantity = array[i+1]
        gender = array[i+2]
        register = {
            'name': name,
            'quantity': quantity,
            'gender': gender
        }

        if gender == 'f':
            names['female'].append(register)
        elif gender == 'm':
            names['male'].append(register)

    return names

names2008 = formatNames(born2008)
names2018 = formatNames(born2018)

#1 La diferencia en cantidad de bebés que existe entre los nombres de misma posición y mismo sexo. Se solicita posición y sexo. (Ver salidas de ejemplo).
def findMayorName(firstNames, secondNames, gender, position):
    oldYear = '2008'
    newYear = '2018'
    mayor = ''
    minor = ''
    year = ''
    diff = 0
    oldName = firstNames[gender][position]
    newName = secondNames[gender][position]
    oldQuantity = int(oldName['quantity'])
    newQuantity = int(newName['quantity'])

    if oldQuantity > newQuantity:
        diff = oldQuantity - newQuantity
        mayor = oldName['name']
        minor = newName['name']
        year = oldYear
    elif newQuantity > oldQuantity:
        diff = newQuantity - oldQuantity
        mayor = newName['name']
        minor = oldName['name']
        year = newYear

    message = ''
    if gender == 'male':
        message = f'Varones en posición #{position}: {diff} nacimientos de varones más del primero del ranking de {year} {mayor} sobre {minor}'
    elif gender == 'female':
        message = f'Mujeres en posición #{position}: {diff} nacimientos de mujeres más del primero del ranking de {year} {mayor} sobre {minor}'
    
    return message

position = 1
gender = 'female'
result = findMayorName(names2008, names2018, gender, position)
print(result)

# 2 Los nombres de todos los bebés que comienzan con la misma letra considerando ambos periodos. Se debe solicitar la letra inicial.
def findNames(yearNames, letter, matchNames):
    for row in yearNames['female']:
        name = row['name']
        
        if name[0] == letter:
            matchNames.append(name)

    for row in yearNames['male']:
        name = row['name']
        
        if name[0] == letter:
            matchNames.append(name)
    
    return matchNames

letter = 'E'
namesMatch = []
namesMatch = findNames(names2008, letter, namesMatch)
namesMatch = findNames(names2018, letter, namesMatch)

names = ' '.join(namesMatch)
print(f'Nombre con {letter}: {names}')

# 3 Los nombres que se repiten en ambos años

def findEqualsNames(firstNames, secondNames):
    matchNames = []

    for row in firstNames['female']:
        name = row['name']

        for row in secondNames['female']:
            if row['name'] == name:
                matchNames.append(name)

    for row in firstNames['male']:
        name = row['name']
        
        for row in secondNames['male']:
            if row['name'] == name:
                matchNames.append(name)
    
    return matchNames

equalNames = findEqualsNames(names2008, names2018)
print(f'Nombres repetidos: {" ".join(equalNames)}')