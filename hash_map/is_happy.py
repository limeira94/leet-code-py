"""
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:
Input: n = 2
Output: false
"""

# 19 -> 81 + 1 = 82
# 82 -> 4 + 64 = 68
# 68 -> 64 + 36 = 100
# 100 -> 0 + 0 + 1 = 1
# Essa solução é diferente pois o time complexity é O(log(n)) e o espaço o mesmo podendo chegar a O(1)
# depois preciso voltar ai para entender melhor como funciona o log(n).
def calc(n: int) -> int:
    curr = 0
    while n > 0:
        digit = n % 10
        curr += digit * digit
        n = n // 10
    return curr

def is_happy(n: int) -> bool:
    seen = set()
    while n != 1:
        n = calc(n)
        if n in seen:
            return False
        seen.add(n)
    return True

def test_1():
    assert is_happy(19) is True


def test_2():
    assert is_happy(2) is False
