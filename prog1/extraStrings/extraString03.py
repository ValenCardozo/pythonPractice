# Tengo una lista con direcciones completas (calle y número).
# Mostrar cada calle y la cantidad de veces que se repite.

records = ['Mitre 1234', '9 de Julio 345', 'Alvear 999', '9 de Julio 11']
addresses = []
unique_addresses = []

for record in records:
    parts = record.split()
    address = ' '.join(parts[:-1])
    addresses.append(address)
    if address not in unique_addresses:
        unique_addresses.append(address)

for address in unique_addresses:
    print(f'{address}: {addresses.count(address)}')
