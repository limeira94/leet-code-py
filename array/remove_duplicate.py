"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates
in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
Consider the number of unique elements in nums to be k. After removing duplicates, return the number of unique elements k.
The first k elements of nums should contain the unique numbers in sorted order.
The remaining elements beyond index k - 1 can be ignored.
"""

from typing import List

# Time complexity O(n) passa uma ver pela lista e Space complexity O(1) pois é realizado in place
def remove_duplicates(nums: List[int]) -> int:
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
    return k


def test_1():
    nums = [1, 1, 2]
    assert remove_duplicates(nums) == 2


def test_2():
    nums = [0,0,1,1,1,2,2,3,3,4]
    assert remove_duplicates(nums) == 5