import timeit

@profile
def gcdLoop(x, y):
    r = x % y
    while r:
        x = y
        y = r
        r = x % y
    return print('GCD with Loop:', y)

@profile
def gcdRecursion(x, y):
    if y > x:
        return gcdRecursion(y, x)

    if x % y == 0:
        return print('GCD with Recursion:', y)

    return gcdRecursion(y, x % y)


def test_loop():
    gcdLoop(123123124, 123131)

def test_recursion():
    gcdRecursion(123123124, 123131)

print(timeit.Timer(test_loop).timeit(number=100))
print(timeit.Timer(test_recursion).timeit(number=100))
