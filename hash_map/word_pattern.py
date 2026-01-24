"""
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Explanation:
The bijection can be established as:
'a' maps to "dog".
'b' maps to "cat".

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""


def word_pattern2(pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words):
        return False

    char_to_word = {}
    word_to_char = {}

    for c, w in zip(pattern, words):
        if c in char_to_word:
            if char_to_word[c] != w:
                return False
        else:
            char_to_word[c] = w

        if w in word_to_char:
            if word_to_char[w] != c:
                return False
        else:
            word_to_char[w] = c
    return True


def word_pattern3(pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words):
        return False

    return len(set(zip(pattern, words))) == len(set(pattern)) == len(set(words))


def word_pattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words):
        return False

    d = {}
    seen = set()
    for i, char in enumerate(pattern):
        if char not in d:
            if words[i] in seen:
                return False
            d[char] = words[i]
            seen.add(words[i])
        else:
            if d[char] != words[i]:
                return False
    return True


def test_1():
    assert word_pattern("abba", "dog cat cat dog") is True


def test_2():
    assert word_pattern("abba", "dog cat cat fish") is False


def test_3():
    assert word_pattern("aaaa", "dog dog dog dog") is True


def test_4():
    assert word_pattern("aaaa", "dog dog dog") is False


def test_5():
    assert word_pattern("abba", "dog dog dog dog") is False
