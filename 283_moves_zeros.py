"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]

"""

from typing import List

"""
Essa solução tempo Time complexity O(n) pois percorremos a lista 1 vez
e o Space Complexity O(1) por fazer tudo no mesmo array
"""


def move_zeroes(nums: List[int]) -> None:
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1
    return nums


def test_1():
    nums = [0, 1, 0, 3, 12]
    assert move_zeroes(nums) == [1, 3, 12, 0, 0]


def test_2():
    nums = [0]
    assert move_zeroes(nums) == [0]
