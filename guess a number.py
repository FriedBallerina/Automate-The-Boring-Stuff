import random

print('I am thinking of a number between 1 and 20.')

too_low = 'Your guess is too low.'
too_high = 'Your guess is too high.'
random_number = random.randint(1, 20)

for guess_taken in range (1, 20):
    guess = int(input('Take a guess.\n'))
    if guess == random_number:
        print('Good job! You guessed my number in ' + str(guess_taken) + ' guesses!')
        break
    elif guess < random_number:
            print(too_low)
    else:
        print(too_high)  