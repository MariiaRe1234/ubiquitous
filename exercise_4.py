"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to
guess the number, then tell them whether they guessed too low, too high, or
exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:
    Keep the game going until the user types “exit”
    Keep track of how many guesses the user has taken, and when the game ends,
    print this out.
    Discussion
Use:
    Modules
    Random numbers
    User input
"""
import random

number = random.randint(1, 9)

while True:
    n = int(input("guess the number between 1 and 9: "))

    if n < number:
        print('your number is too low')
        continue
    elif n > number:
        print('your number is too high')
        continue
    else:
        print(f'you are right, it is the number {number}')
        break
