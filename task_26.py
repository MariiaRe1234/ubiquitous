"""
Write a Python program that takes a list of numbers and finds the
second largest number in the list.

Requirements:
If the list contains fewer than two unique numbers, the program should
raise an error
If there are enough values, the program should find and display the
second largest number
Ignore all non-number values

Validation rules:
Not enough values or empty list
Items in a list are not numbers

Hints:
Use set() to remove duplicate numbers.
Sort the list and access the second largest value using indexing
"""
ll = [True, 'cat', 3.5, 24, 52.2, '34', 'oranges', bool, 14, None, 48.5 ]

def sort_int(res):
    new_res = []
    for i in res:
        if isinstance(i, (int, float)):
            new_res.append(i)

        # try:
        #     new_res.append(int(i))
        # except (TypeError, ValueError):
        #     pass

    return new_res

unique_numbers = sorted(list(set(sort_int(ll))))


if len(unique_numbers) < 2:
    raise ValueError

print(unique_numbers[-2])




