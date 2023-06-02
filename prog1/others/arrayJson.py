import json

array = []

for i in range(5):
    name = input('entry name: ')
    lastName = input('entry last name: ')
    age = int(input('entry age: '))

    object = {
        "name":  name,
        "lastName": lastName,
        "age": age
    }

    array.append(object)

print(array)