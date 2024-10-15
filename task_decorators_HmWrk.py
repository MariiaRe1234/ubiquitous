"""
Implement the @timeit() decorator that can take an optional parameter threshold.

Example:

@timeit(threshold=0.5)
def some_heavy_function():
    # complex code goes here
    pass

@timeit()
def another_function():
    pass


Notes:

The threshold parameter takes a value in seconds.
The decorator should print the execution time if it exceeds the value specified in threshold.
If threshold is not specified, the decorator should print any execution time.
"""
import time



def timeit(threshold=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            if threshold is None or elapsed_time > threshold:
                print(f'Function {func.__name__} took {elapsed_time:.2f} sec')
            return result
        return wrapper
    return decorator


@timeit(threshold=1.5)
def heavy_function(n=50000000):
    res = 0
    for i in range(0, n + 1):
        res += i
    return res

@timeit()
def another_function(n=500000):
    res = 0
    for i in range(0, n + 1):
        res += i
    return res



heavy_function()
another_function()
