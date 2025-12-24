"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""

from typing import List

"""
Time Complexity O(n^2)
Space Complexity O(n) because I'm using sort
"""


def three_sum(nums: List[int]) -> List[int]:
    # nums = [-1, 0, 1, 2, -1, -4]
    nums.sort()
    n = len(nums)
    answer = []
    for i in range(n):
        if nums[i] > 0:
            break
        elif i > 0 and nums[i] == nums[i - 1]:
            continue

        lo, hi = i + 1, n - 1
        while lo < hi:
            summ = nums[i] + nums[lo] + nums[hi]
            if summ == 0:
                answer.append([nums[i], nums[lo], nums[hi]])
                lo, hi = lo + 1, hi - 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
                while lo < hi and nums[hi] == nums[hi + 1]:
                    hi -= 1

            elif summ < 0:
                lo += 1
            else:
                hi -= 1
    return answer


def test_1():
    nums = [-1, 0, 1, 2, -1, -4]
    assert three_sum(nums) == [[-1, -1, 2], [-1, 0, 1]]


def test_2():
    nums = [0, 0, 0]
    assert three_sum(nums) == [[0, 0, 0]]


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    three_sum(nums)
