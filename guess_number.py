from __future__ import barry_as_FLUFL
import random

print('I am thinking of a number between 1 and 30, take a guess')
right_guess = random.randint(1, 30)
counter = 0

while True:
    guess = input('Enter your guess:')
    guess_int = int(guess)
    counter = counter + 1
    
    if guess_int > right_guess:
        print('Too high')
        continue
    elif guess_int < right_guess:
        print('Too low')
        continue
    else:
        break
print(f'Good job!. You got it in {counter} guesses')
