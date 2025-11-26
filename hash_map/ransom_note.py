"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""

from collections import Counter

"""
Time complexity O(n)
Space complexioty O(n) pode ser O(1) pelo numero ser fixo ou seja apenas temos 26 caracteres pois especifica
que são letras minusculas
"""
def can_construct2(ransom_note: str, magazine: str) -> bool:
    hash_r = {}
    hash_m = {}
    for char in ransom_note:
        if char not in hash_r:
            hash_r[char] = 1
        else:
            hash_r[char] += 1

    for char in magazine:
        if char not in hash_m:
            hash_m[char] = 1
        else:
            hash_m[char] += 1

    for char in hash_r:
        if hash_m.get(char, 0) < hash_r[char]:
            return False
    return True


"""
Time complexity O(n)
Space complexity O(1) -> por ser limitador a letras do alfaberto 26
"""
def can_construct(ransom_note: str, magazine: str) -> bool:
    char_count = Counter(magazine)

    for char in ransom_note:
        char_count[char] -= 1
        if char_count[char] < 0:
            return False
    return True


def test_1():
    assert can_construct("a", "b") is False


def test_2():
    assert can_construct("aa", "abd") is False


def test_3():
    assert can_construct("aa", "aab") is True
