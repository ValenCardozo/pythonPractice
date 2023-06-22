# Validar un número con la posibilidad de tener un rango
# (reutilizar inputInt/inputFloat o bien inputNumber si prefieren usar una sola función para validar ambos tipos de datos)

def inputNumber(type, message: str, insult:str, minimum: int=0, maximun: int=1000):
    validate = False
    while not validate:
        number = input(message)
        try:
            number = type(number)
            if minimum <= number <= maximun:
                validate = True
        except:
            print(insult)
    
    return number

number = inputNumber(int, 'Ingrese un numero: ', 'Un numero imbecil', 0, 10)
print(number)