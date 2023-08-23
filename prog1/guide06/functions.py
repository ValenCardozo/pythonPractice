# Validacion de ingreso de numeros enteros
def inputInteger(message: str, insult: str):
    validate = False
    while not validate:
        number = input(message)
        try:
            number = int(number)
            validate = True
        except:
            print(insult)

    return number

def inputFloat(message: str, insult: str):
    validate = False
    while not validate:
        number = float(message)
        try:
            number = int(number)
            validate = True
        except:
            print(insult)

    return number

# El comandante ford
def foo():
    print('MEAAAAAAAMEEEEEEE')

# Funcion con multiples argumentos
def function(*args):
    print(args)

# Funcion con valores por defecto
def hello(message: str, city: str='Rio Cuarto'):
    print(message + ' ' + city)

# Funcion que junta todas las opciones
def complex(first, second, *args, named='named'):
    print(first, second, args, named)

# Funcion que tiene argumentos multiples denominados por clave
def keys(**kwargs):
    print(kwargs['hi'], kwargs['hellow'])

# keys(hi='motherfuckers', hellow='son of bitch')

def inputInt(msg, mini=-10**308, maxi=10**308):
    validado = False
    while not validado:
        try:
            n = int(input(msg))
            if mini <= n <= maxi:
                validado = True
            else:
                print('fuera de rango')
        except:
            print('ingreso inválido')
    return n