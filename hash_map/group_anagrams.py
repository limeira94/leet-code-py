"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""

from collections import defaultdict
from typing import List


"""
    {
        "aet" : ["eat", "tea", "ate"]
        "ant" : ["tan", "nat"]
        "abt": ["bat]
    }
"""


def group_anagrams(strs: List[str]) -> List[List[str]]:
    dic = defaultdict(list)
    for word in strs:
        dic["".join(sorted(word))].append(word)
    return list(dic.values())


def group_anagrams2(strs: List[str]) -> list[List[str]]:
    dic = {}

    for word in strs:
        key = "".join(sorted(word))
        if key not in dic:
            dic[key] = []
        dic[key].append(word)
    return list(dic.values())


def group_anagrams3(strs: List[str]) -> list[List[str]]:
    dic = {}

    for word in strs:
        key = "".join(sorted(word))
        dic.setdefault(key, []).append(word)
    return list(dic.values())


def test_1():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    assert group_anagrams(strs) == [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]


def test_2():
    strs = [""]
    assert group_anagrams(strs) == [[""]]


def test_3():
    strs = ["a"]
    assert group_anagrams(strs) == [["a"]]


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    group_anagrams(strs)
