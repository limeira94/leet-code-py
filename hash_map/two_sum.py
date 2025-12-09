"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    # 0, 2
    # 1, 7
    # 2, 11
    # 3, 15
    for i, num in enumerate(nums):
        if target - num in hashmap:
            return [hashmap[target - num], i]
        hashmap[num] = i


def test_1():
    nums = [2, 7, 11, 15]
    target = 9
    assert two_sum(nums, target) == [0, 1]


if __name__ == "__main__":
    nums = [2, 3, 7, 15]
    target = 9
    two_sum(nums, target)
