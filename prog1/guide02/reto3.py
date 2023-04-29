# Reto 3
# Escribe un programa que muestre la hora cada quince minutos, desde las 12 am hasta las 11.45 pm

dayHours = 24
halfDay = (dayHours / 2) * 4
halfHours = dayHours * 4
hour = 12
minut = 0
horaryUse = 'am'
hourShow = hour
minutShow = '00'

for i in range(halfHours):
    print(f'{hourShow}:{minutShow} {horaryUse}')
    
    if minut + 15 == 60:
        minut = 0
    
        if hour == 12:
            hour = 1
        else:
            hour = hour + 1
    else:
        minut = minut + 15

    minutShow = minut
    if minut == 0:
        minutShow = '00'

    hourShow = hour
    if hour < 10:
        hourShow = '0' + str(hour)
    
    if i == halfDay - 1:
        horaryUse = 'pm'
    
    


