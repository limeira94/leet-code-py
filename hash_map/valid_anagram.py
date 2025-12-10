"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""

from collections import Counter


def is_anagram4(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    hash_s = Counter(s)
    hash_t = Counter(t)

    if hash_s == hash_t:
        return True
    return False


def is_anagram2(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


def is_anagram3(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


def is_anagram(s: str, t: str) -> bool:
    s_count = Counter(s)
    for char in t:
        if char not in s_count:
            return False
        s_count[char] -= 1
        if s_count[char] == 0:
            del s_count[char]

    return True


def test_1():
    s = "anagram"
    t = "nagaram"
    assert is_anagram(s, t) is True


def test_2():
    s = "rat"
    t = "car"
    assert is_anagram(s, t) is False
