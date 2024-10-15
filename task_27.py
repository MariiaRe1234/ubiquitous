"""
Write a Python function that takes a predefined list of numbers and separates
them into two lists: one containing all the even numbers and the other
containing all the odd numbers. The function should return both lists.

Requirements:
The function should be called separate(numbers) and accept a list of integers
as an argument.
The function should create two separate lists:
One for even numbers.
One for odd numbers.
The function should return both lists (even and odd).

Requirement:
Implement 2 different solutions: using for loop and list comprehensions
"""

numbers = [10, 34, 22, 53.3, 42, 9.2, 68, 75, 13, 48.14]


def separate(num):
    even = []
    odd = []
    for i in num:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd


even1, odd1 = separate(numbers)  # как это работает?
print(f"Even numbers: {even1}")
print(f"Odd numbers: {odd1}")


def separate(numbers0):
    even_n = [i for i in numbers0 if i % 2 == 0]
    odd_n = [i for i in numbers0 if i % 2 != 0]
    return even_n, odd_n


even_n1, odd_n1 = separate(numbers)
print(f"Even numbers: {even_n1}")
print(f"Odd numbers: {odd_n1}")
