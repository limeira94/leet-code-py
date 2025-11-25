"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

import re

"""
Aqui tem um problema, no espaço de complexidade
Time complexity e o Space complexity ambos são O(n)
Porém existe uma solução que faz o Space ser O(1)
o problema está na função regex, cria uma nova string.
"""


def is_palindrome2(s: str) -> bool:
    clean_s = re.sub(r"[^a-zA-Z0-9]", "", s)
    clean_s = clean_s.lower()
    left = 0
    right = len(clean_s) - 1
    while left <= right:
        if clean_s[left] != clean_s[right]:
            return False
        left += 1
        right -= 1
    return True


def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


def test_1():
    s = "abccba"
    assert is_palindrome(s) is True


def test_2():
    s = "A man, a plan, a canal: Panama"
    assert is_palindrome(s) is True


def test_3():
    s = "race a car"
    assert is_palindrome(s) is False


def test_4():
    s = " "
    assert is_palindrome(s) is True
