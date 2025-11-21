"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

# Solução Time complexity -> 0(n^2) Spance Complexity -> O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
            
# Solution Time complexity -> O(n) Space Complexity -> O(n)           
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [10, 20, 30], target = 40
        num_dict = {}
        for i, num in enumerate(nums):
            if target - num in num_dict:
                return [num_dict[target - num], i]
            num_dict[num] = i
            
        # {10: 0}
        # {10: 0, 20: 1}
        # {10: 0, 20: 1, 30: 2}