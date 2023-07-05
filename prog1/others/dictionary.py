# Diccionarios tipo registro
relations = {
    'nombre': 'Ana',
    'hijos': [
        'Hugo',
        'Paco'
    ]
}

shorts = {
    'rojas': 2,
    'verdes': 11,
    'azules': 8
}

persons = {
    {
        'nombre': 'Ana',
        'hijos': [
            'Hugo',
            'Paco'
        ]
    },
    {
       'nombre': 'Ana',
        'hijos': [
            'Hugo',
            'Paco'
        ]
    },
    {
        'nombre': 'Ana',
        'hijos': [
            'Hugo',
            'Paco'
        ]
    }
}

# Acceder a un valor, mediante el indice
print(relations['hijos']);

# Agregar indices y valores
relations['cantidadHijos'] = 2

# Eliminar indices
del relations['cantidadHijos']
relations.pop('cantidadHijos')

# Recorrer un diccionario
# Claves solamente
for key in relations.keys():
    print(key)
# Valores solamente
for value in relations.values():
    print(value)
# Clave - valor al mismo tiempo.
for key, value in relations.items():
    print(key, value)