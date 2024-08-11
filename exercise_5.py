"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

Write a program that returns a list that contains only the elements that are
common between the lists (without duplicates).

Make sure your program works on two lists of different sizes.

Write this in one line of Python using at least one list comprehension.

*I've also desided to random generate this two lists
"""
import random


a = random.sample(range(100), 15)
b = random.sample(range(100), 15)

def comparison(l1, l2):
    return list(set(i for i in l1 if i in l2))

print(a)
print(b)
print(comparison(a, b))