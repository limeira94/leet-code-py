"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:
Input: arr = [1,2]
Output: false

Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
"""

from typing import List
from collections import Counter


def unique_occurrences(arr: List[int]) -> bool:
    arr_hm = Counter(arr)
    # arr_m = {1:3, 2:2, 3:1}
    values = arr_hm.values()
    if len(values) == len(set(values)):
        return True
    return False


def test_1():
    arr = [1, 2, 2, 1, 1, 3]
    assert unique_occurrences(arr) is True


def test_2():
    arr = [1, 2]
    assert unique_occurrences(arr) is False


def test_3():
    arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    assert unique_occurrences(arr) is True
