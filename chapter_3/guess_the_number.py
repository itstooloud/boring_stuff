# this is a number guessing game

import random

secretNumber = random.randint(1, 20)
print('Guess a number between one and twenty.')

for guessesTaken in range(1,7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break #this condition is the correct guess

if guess == secretNumber:
    print('Great job! It took you ' + str(guessesTaken) + ' tries.')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))

    

