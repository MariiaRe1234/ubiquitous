"""
Find min. and max. value

Consider a list of values:

items = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]

Tasks:
1. Convert elements to integer. Find min and max value from list
2. Give answer to following questions:
    - which exception we should except when converting value to int() ?

Notes:
 - use try/except
 - use built-in functions min() and max()

https://docs.python.org/3/library/functions.html#min
https://docs.python.org/3/library/functions.html#max
"""


items = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]

def converted(numbers):
    res = []
    for i in numbers:
        try:
            res.append(int(i))
        except (ValueError, TypeError):
            continue
    return res

