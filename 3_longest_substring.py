"""
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

# Solution 1
# Time Complexity O(n)
# Space Complexity O(m)
"""
Nesse caso o tempo é O(n), por mais que tenha dois whiles isso nao indica quadratico, 
o que indicaria era se os ponteiros voltassem os seus índices, nesse caso não pode retroceder 
"""


def length_longest_substring(s: str) -> int:
    max_len = 0
    hash_set = set()
    left = right = 0
    while right < len(s):
        while s[right] in hash_set:
            hash_set.remove(s[left])
            left += 1
        hash_set.add(s[right])
        max_len = max(max_len, right - left + 1)
        right += 1
    return max_len


def length_longest_substring2(s: str) -> int:
    max_len = 0
    char_map = {}
    left = 0
    for right in range(len(s)):
        char = s[right]
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
        char_map[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len


def test_1():
    s = "abcabcbb"
    assert length_longest_substring(s) == 3


def test_2():
    s = "bbbbbbb"
    assert length_longest_substring(s) == 1


def test_3():
    s = "pwwkew"
    assert length_longest_substring(s) == 3
