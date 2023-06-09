# Escribe una función que encuentre el número que más se repite en una lista

def numberMoreRepeat(numbers: list):
    moreRepeat = ''
    maxRepeat = 0
    for number in numbers:
        if numbers.count(number) > maxRepeat:
            maxRepeat = numbers.count(number)
            moreRepeat = number

    return moreRepeat

def onlyNumbers(text: str):
    numbers = ''
    for caracter in text:
        if 48 <= ord(caracter) <= 57:
            numbers += caracter

    return numbers

numbers = onlyNumbers('23131edqwdqdosndfoan12313131312313')
print(numberMoreRepeat(numbers))