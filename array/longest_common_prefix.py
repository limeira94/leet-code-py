"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
"""

from typing import List


# time O(n * m) -> n is number of string and m o min_length
# space O(1) not have memory allocation
def longest_common_prefix(strs: List[str]) -> str:
    min_length = float("inf")
    
    for s in strs:
        if len(s) < min_length:
            min_length = len(s)

    i = 0
    while i < min_length:
        for s in strs:
            if s[i] != strs[0][i]:
                return s[:i]    
        i += 1
    
    return s[:i]

def test_1():
    strs = ["flower", "flow", "flight"]
    assert longest_common_prefix(strs) == "fl"


def test_2():
    strs = ["dog", "racecar", "car"]
    assert longest_common_prefix(strs) == ""
