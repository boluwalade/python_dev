import random
import sys

print('ROCK,PAPER,SCISSOR')

win = 0
loss = 0
draw = 0

while True:
    print(f'{win} wins, {draw} draws and {loss} loss')
    #player move
    while True:
        player_move = input('Enter your play - (r)ock (p)aper (s)cissors:\n').lower()
        if player_move == 'q':
            sys.exit()
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break
        print('Non valid entry. Enter r,p or c')

    if player_move == 'r':
        print('ROCK VS ...')
    elif player_move == 'p':
        print('PAPER VS...')
    elif player_move == 's':
        print('SCISSORS VS ....')

    #computer move
    randoms = random.randint(1,3)
    if randoms == 1:
        computer_move = 'r'
        print('ROCK')
    elif randoms == 2:
        computer_move = 'p'
        print('PAPER')
    elif randoms == 3:
        computer_move = 's'
        print('SCISSORS')
    
    #Game logic
    if player_move == computer_move:
        print('DRAW')
        draw = draw + 1
    elif player_move == 'r' and computer_move == 's':
        print('YOU WIN !')
        win = win + 1
    elif player_move == 'p' and computer_move == 'r':
        print('YOU WIN !')
        win = win + 1
    elif player_move == 's' and computer_move == 'p':
        print('YOU WIN !')
        win = win + 1
    elif player_move == 'r' and computer_move == 'p':
        print('YOU LOSE !')
        loss = loss + 1
    elif player_move == 'p' and computer_move == 's':
        print('YOU LOSE !')
        loss = loss + 1
    elif player_move == 's' and computer_move == 'r':
        print('YOU LOSE !')
        loss = loss + 1