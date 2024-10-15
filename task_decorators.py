import time


def ffff(funk):

    def wraper(*args, **kwargs):
        return funk(*args, **kwargs)
    return wraper

@ffff
def factorial(n=50000000):
    res = 0
    for i in range(0, n+1):
        res += i
    return res


if __name__ == '__main__':
    start = time.time()
    res = factorial(n=30000000)
    end = time.time()
    print(res)
    print(round(end - start, 1))