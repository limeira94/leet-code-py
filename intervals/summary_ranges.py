"""
You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges, and there is no integer
x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
"""

from typing import List


def summary_ranges(nums: List[int]) -> List[str]:
    answer = []
    n = len(nums)
    i = 0
    while i < n:
        start = nums[i]

        while i < n - 1 and nums[i] + 1 == nums[i + 1]:
            i += 1
        if start != nums[i]:
            answer.append(f"{start}->{nums[i]}")
        else:
            answer.append(f"{start}")
        i += 1
    return answer


def test_1():
    nums = [0, 1, 2, 4, 5, 7]
    assert summary_ranges(nums) == ["0->2", "4->5", "7"]


if __name__ == "__main__":
    nums = [0, 1, 2, 4, 5, 7]
    summary_ranges(nums)
