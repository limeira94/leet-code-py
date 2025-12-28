"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3
"""

from typing import List
from collections import Counter


def majority_element2(nums: List[int]) -> int:
    hashmap = {}
    for num in nums:
        if num in hashmap:
            hashmap[num] += 1
        else:
            hashmap[num] = 1

    max_value = 0
    ans = -1
    for key, val in hashmap.items():
        if val > max_value:
            max_value = val
            ans = key

    return ans


def majority_element3(nums: List[int]) -> int:
    c_nums = Counter(nums)
    max_value = 0
    ans = -1
    for key, val in c_nums.items():
        if val > max_value:
            max_value = val
            ans = key
    return ans

# Time Complexity 0(n) Space complexity O(1)
def majority_element(nums: List[int]) -> int:
    ans = -1
    count = 0
    for num in nums:
        if count == 0:
            ans = num

        if ans == num:
            count += 1
        else:
            count -= 1
    return ans


def test_1():
    nums = [2, 2, 3, 3, 4, 1, 1, 1]
    assert majority_element(nums) == 1


def test_2():
    nums = [0, 0, 0, 1, 1]
    assert majority_element(nums) == 0
