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


def length_longest_substring(s: str) -> int:
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


def length_longest_substring2(s: str) -> int:
    left = 0
    longest = 0
    sett = set()
    n = len(s)

    for right in range(n):
        while s[right] in sett:
            sett.remove(s[right])
            left += 1

        w = right - left + 1
        longest = max(longest, w)
        sett.add(s[right])
    return longest


def test_1():
    s = "abcabcbb"
    assert length_longest_substring(s) == 3


if __name__ == "__main__":
    s = "abcabcbb"
    length_longest_substring2(s)
