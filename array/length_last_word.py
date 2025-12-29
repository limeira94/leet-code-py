"""
Given a string s consisting of words and spaces, return the length of the last word in the string.s
A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
"""


# Time complexity O(n) because use split, Space complexity O(n) because have a list, o len é ums struct do C because is a CPython
def length_last_word2(s: str) -> int:
    return len(s.split()[-1])

# time complexity O(n) and Space complexity O(1) 
def length_last_word(s: str) -> int:
    i = len(s) - 1
    count = 0

    while i >= 0 and s[i] == " ":
        i -= 1

    while i >= 0 and s[i] != " ":
        count += 1
        i -= 1
    return count


def test_1():
    s = "Hello World"
    assert length_last_word(s) == 5
