"""
Given an integer array nums and an integer k, return true if there are two distinct indices i
and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

from typing import List


def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    hashmap = {}
    for i, num in enumerate(nums):
        if num in hashmap and i - hashmap[num] <= k:
            return True
        hashmap[num] = i
    return False


def test_1():
    nums = [1, 2, 3, 4, 1, 1]
    k = 3
    assert contains_nearby_duplicate(nums, k) is True


def test_2():
    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    assert contains_nearby_duplicate(nums, k) is False
