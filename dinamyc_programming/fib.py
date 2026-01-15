def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)


# problem this solutions is Time O(n2) and Space O(n)
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...


def fib_memo(n):
    memo = {}
    return _fib(n, memo)


def _fib(n, memo):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = _fib(n - 2, memo) + _fib(n - 1, memo)
    return memo[n]
# Time O(n) Space(O)

print(fib_memo(1))
print(fib_memo(2))
print(fib_memo(3))
print(fib_memo(4))
print(fib_memo(5))
print(fib_memo(6))
print(fib_memo(7))
