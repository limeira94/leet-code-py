"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

from typing import List

"""
Por mais que passe nos teste essa solução é ineficiente, pois temos o count e remove que itera sobre a lista,
podendo ser um O(n^2)
"""


def remove_element2(nums: List[int], val: int) -> int:
    while nums.count(val):
        nums.remove(val)
    k = len(nums)
    return k

"""
Time complexity O(n) pois passo pela lista 1 vez.
Space complexity O(1), apenas utilio duas variavís k, e i.
"""
def remove_element(nums: List[int], val: int) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


def test_1():
    nums = [3, 2, 2, 3]
    val = 3
    assert remove_element(nums, val) == 2


def test_2():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    assert remove_element(nums, val) == 5
