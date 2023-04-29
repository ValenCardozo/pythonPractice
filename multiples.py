# Generar una lista con los primeros 10 multiplos de 3

number = 3
multiples = []

for i in range(10):
    multiple = number * (i + 1)
    multiples.append(multiple)

print(f'Los 10 primero multiplos de {number} son {multiples}')

