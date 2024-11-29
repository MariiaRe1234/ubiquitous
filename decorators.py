from functools import wraps


def decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Before call')
        res = func(*args, **kwargs)
        print('After call')
        return res
    return wrapper

@decorator
def multiply_digits(x, y):
    print(x/y)

multiply_digits(7254, 0)