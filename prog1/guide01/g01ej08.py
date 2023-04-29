# Ejercicio 8
# Pasar un período expresado en segundos a un período
# expresado en días, horas, minutos y segundos.

initSeconds = int(input('Ingrese tiempo expresado en segundos: '))

days = initSeconds // 86400
seconds = initSeconds % 86400
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

print(f" dias: {days}, horas: {hours}, minutos: {minutes}, segundos: {seconds}")

# minuts = seconds // 60
# restSeconds = seconds - minuts * 60
# hours = minuts // 60
# restMinuts = minuts - hours * 60
# days = hours // 24
# restHours = hours - days * 24
# print(f" dias: {days}, horas: {restHours}, minutos: {restMinuts}, segundos: {restSeconds}")