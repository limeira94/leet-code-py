"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3
"""

from typing import List


def longest_consecutive(nums: List[int]) -> int:
    sett = set(nums)
    longest = 0
    for num in sett:
        if num - 1 not in sett:
            length = 1
            while num + length in sett:
                length += 1

            longest = max(length, longest)

    return longest


def test_1():
    nums = [100, 4, 200, 1, 3, 2]
    assert longest_consecutive(nums) == 4


def test_2():
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    assert longest_consecutive(nums) == 9


def test_3():
    nums = [1, 0, 1, 2]
    assert longest_consecutive(nums) == 3
