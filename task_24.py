"""
Create a simple number guessing game in Python where the program generates a random number between 1 and 100, and the user has to guess the number. The program should give feedback to the user after each guess by telling them whether their guess is too high, too low, or correct.

Requirements:
The program should generate a random number between 1 and 100.
The user is allowed up to 7 guesses to find the correct number.
After each guess, the program should indicate whether the guess was too high, too low, or correct.
If the user guesses correctly, congratulate them and exit the program.
If the user fails to guess the number in 7 tries, reveal the correct number and end the game.
The program should handle invalid inputs (e.g., non-numeric values).

Hints:
Use random.randint(1, 101) to generate a random number.
Use a while True loop.
Use input validation to handle non-numeric values.
"""
import random

number = random.randint(1, 101)
a = 1
while a < 8:
    a += 1

    n = int(input("guess the number between 1 and 100: "))
    if n == number:
        print(f'you are correct, congratulations! the number was {number}')
        break
    elif n < number:
        print('your number is too low')
        continue
    elif n > number:
        print('your number is too high')
        continue
print(f"the hide number was {number}")


