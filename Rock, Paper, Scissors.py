# Rock, Paper, Scissors
import random

def began():
    start_game = input('Would you like to play a game? ')
    while start_game.upper() != 'YES' or 'NO':
        if start_game.upper() == 'YES':
            game()
        elif start_game.upper() == 'NO':
            exit()
        else:
            print('That response does not seem right!')
            start_game = input('Would you like to play a game? ')
            
def game():
    playerwin = 0
    computerwin = 0
    options = ['Rock', 'Paper', 'Scissors']
    while True:
        computerpick = random.choice(options)
        playerpick = input('Rock, Paper, or Scissors? ').capitalize()
        if playerpick == 'Rock' and computerpick == 'Scissors':
            print('You chose Rock. The computer chose Scissors. You won!')
            playerwin += 1
        elif playerpick == 'Rock' and computerpick == 'Paper':
            print('You chose Rock. The computer chose Paper. You lost!')
            computerwin += 1
        elif playerpick == 'Paper' and computerpick == 'Scissors':
            print('You chose Paper. The computer chose Scissors. You lost!')
            computerwin += 1
        elif playerpick == 'Paper' and computerpick == 'Rock':
            print('You chose Paper. The computer chose Rock. You won!')
            playerwin += 1
        elif playerpick == 'Scissors' and computerpick == 'Paper':
            print('You chose Scissors. The computer chose Paper. You won!')
            playerwin += 1
        elif playerpick == 'Scissors' and computerpick == 'Rock':
            print('You chose Scissors. The computer chose Rock. You lost!')
            computerwin += 1
        elif playerpick == computerpick:
            print(f'You chose {playerpick}. The computer chose {computerpick}. It is a tie!')
        elif playerpick == 'Quit' and playerwin == 1 and computerwin == 1:
            print(f'You won {playerwin} time. The computer won {computerwin} time.')
            exit()
        elif playerpick == 'Quit' and playerwin == 1:
            print(f'You won {playerwin} time. The computer won {computerwin} times.')
            exit()
        elif playerpick == 'Quit' and computerwin == 1:
            print(f'You won {playerwin} times. The computer won {computerwin} time.')
            exit()
        elif playerpick == 'Quit':
            print(f'You won {playerwin} times. The computer won {computerwin} times.')
            exit()
        else:
            print('That response does not seem right!')

began()