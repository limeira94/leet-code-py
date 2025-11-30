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

# Time complexity O(n) pois passa pela string uma única vez
# O Space complexity é O(1) pois nao estou construindo uma estrutura de dados especifica e vai ser constante.
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
