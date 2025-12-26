"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
"""


def roman_to_int(s: str) -> int:
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    summ = 0
    n = len(s)
    i = 0

    while i < n:
        if i < n - 1 and d[s[i]] < d[s[i + 1]]:
            summ += d[s[i + 1]] - d[s[i]]
            i += 2
        else:
            summ += d[s[i]]
            i += 1
    return summ


def test_1():
    s = "LVIII"
    assert roman_to_int(s) == 58


def test_2():
    s = "MCMXCIV"
    assert roman_to_int(s) == 1994
