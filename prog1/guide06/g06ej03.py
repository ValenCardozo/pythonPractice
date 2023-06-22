# Implemente una función que calcule el promedio de una cantidad variable de números.
# Se tiene que poder pasar un argumento que descarte los valores negativos para sacar dicho promedio.

def promedio(*numbers: int, sinNegativos=False):
    negativeNumbers = 0
    acumulator = 0
    for number in numbers:
        if sinNegativos:
            if number > 0:
                acumulator += number
            else:
                negativeNumbers += 1
        else:
            acumulator += number
    
    return acumulator / (len(numbers) - negativeNumbers)


print(promedio(121,65,-88,34,-9,27)) # 150/6=25
print(promedio(121,65,-88,34,-9,27, sinNegativos=True)) # 247/4=61.75
print(promedio(2,4)) # 3
