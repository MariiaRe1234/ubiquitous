"""
Greeting function
=====

Implement function that takes 'name' as argument and returns text:

Implement 3 different solutions:
 - format string using C-style
 - using .format() method
 - using F-string

Useful links:
 - https://www.pythoncheatsheet.org/cheatsheet/string-formatting
"""

day = 'monday'


def greeting_c_style(name, age):
    """C-style string formatting with %s (old, rarely used)"""
    return 'Hello, my name is %s. I am %s years old!' % (name, age)


def greeting_with_format(name, age):
    return 'Hello, my name is {name}. I am {age} years old!'.format(name=name, age=age)


def greeting_fstring(name, age):
    """F-string, introduced in Python 3"""
    return f"Hello, my name is {name}. I am {age} years old! Today is {day}"

if __name__ == '__main__':
    print(greeting_c_style('Billy', 20))
    print(greeting_with_format('Billy', 20))
    print(greeting_fstring('Billy', 20))