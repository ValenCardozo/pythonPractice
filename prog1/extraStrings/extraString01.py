#Transformar esta cadena a dos listas paralelas de nombres y sueldos(sin el signo pesos):
#“Juan$120000,Ana$250000,Luis$76500,Vilma$98700”. Mostrar las listas resultantes completas.

string = 'Juan$120000,Ana$250000,Luis$76500,Vilma$98700'

registers = string.split(',')
names =[]
amounts = []

for register in registers:
    sign = register.find('$')
    name = register[:sign - 1]
    amount = register[sign + 1:]

    names.append(name)
    amounts.append(amount)

print(names)
print(amounts)