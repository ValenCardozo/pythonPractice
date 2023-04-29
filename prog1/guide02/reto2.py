# Reto 2
# Programa el juego Piedra-Papel-Tijera. 
# Una vez funcionando se modifica para que gane el que llegue a 3 triunfos.

from random import choice

winsForComputer = 0
winsForUser = 0
finish = 0

while finish == 0:
    userChoice = input('Ingrese una opcion: piedra, papel o tijera ')
    computerChoice = choice(['piedra', 'papel', 'tijera'])
    print(computerChoice)

    itsDraw = userChoice == computerChoice

    userWins = (userChoice == 'piedra' and computerChoice == 'tijera') or (userChoice == 'tijera' and computerChoice == 'papel') or (userChoice == 'papel' and computerChoice == 'piedra')

    if itsDraw:
        print('Empate!')
    elif userWins:
        print('Usted gana!')
        winsForUser = winsForUser + 1
    else:
        print('La computadora gana!')
        winsForComputer = winsForComputer + 1
    
    if winsForUser == 3:
        print('El usuario gano el desafio')
        finish = 1
    elif winsForComputer == 3:
        print('La computadora gano el desafio')
        finish = 1
