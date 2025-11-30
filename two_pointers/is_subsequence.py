"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting
some (can be none) of the characters without disturbing the relative positions of the remaining
characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
"""


# O(n) time complexity and O(1) space complexity, como não existe criação de estrutura de dados o espaço é constante
def is_subsequence(s: str, t: str) -> bool:
    if not s:
        return True
    i = 0
    for char in t:
        if char == s[i]:
            i += 1
        if i == len(s):
            return True
    return False


def test_1():
    assert is_subsequence("abc", "ahbgdc") is True


def test_2():
    assert is_subsequence("axc", "ahbgdc") is False


def test_3():
    assert is_subsequence("acb", "ahbgdc") is False
