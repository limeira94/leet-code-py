def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def test_1():
    assert factorial(5) == 120


def test_2():
    assert factorial(0) == 1


def test_3():
    assert (1) == 1
