# Escribe una función que determine si dos listas tienen algún elemento en común

def loadList(limit: int):
    array = []
    for i in range(limit):
        element = input('Ingrese un elemento: ')
        array.append(element)

    return array

def shareElementInList(firstList: list, secondList: list):
    shareElement = False
    for element in firstList:
        if element in secondList:
            shareElement = True
    
    return shareElement

firstList = loadList(3)
secondList = loadList(3)

print(shareElementInList(firstList, secondList))


