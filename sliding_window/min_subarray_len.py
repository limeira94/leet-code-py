"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""

from typing import List


def min_subarray_len(target: int, nums: List[int]) -> int:
    left = 0
    current_sum = 0
    min_len = float("inf")

    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_len if min_len != float("inf") else 0


def test_1():
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    assert min_subarray_len(target, nums) == 2


def test_2():
    target = 4
    nums = [1, 4, 4]
    assert min_subarray_len(target, nums) == 1


def test_3():
    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert min_subarray_len(target, nums) == 0
