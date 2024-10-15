"""
Multiples of 3 and 5. Find the best algorithm
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 100000000.
"""

def sum_up(num):
    res = 0
    for i in range(num):
        current = res
        if i % 3 == 0 or i % 5 == 0:
            res += i
        num += 1
        if res >= 100000000:
            return current
    return res
print(sum_up(100000000))