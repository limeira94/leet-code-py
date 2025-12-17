from typing import List


def min_subarray_len(target: int, nums: List[int]) -> int:
    left = 0
    cur_sum = 0
    min_len = float("inf")
    for right in range(len(nums)):
        cur_sum += nums[right]

        while cur_sum >= target:
            min_len = min(min_len, right - left + 1)
            cur_sum -= nums[left]
            left += 1

    return min_len if min_len != float("inf") else 0


"""
nums = [2, 3, 1, 2, 4, 3], target = 7, output: 3

1. 2 + 3 + 1 + 2 = 8 -> 
    8 >= target --> 
    min_len = (float(inf), 4) = 4 --> 
    cur_sum = 6
    left = 1
2. 6 + 4 = 10
    10 >= target
    min_len(inf, 4 - 1 + 1) = 4
    cur_sum = 7
    left = 2
3. 7 >= target
    min_len(inf, 4 - 2 + 1) = 3
    cur_sum = 6
    left = 3
4. 6 + 3 = 9
    9 >= target:
    min_len = float(inf), 5 - 3 + 1 = 3
    cur_sum = 7
    left = 4
5. 7 >= target:
    min_len = float(inf), 5 - 4 + 1 = 2
    cur_sum = 3
    left = 5

responde => 2
"""


def test_1():
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    assert min_subarray_len(target, nums) == 2


def length_longest_substring(s: str) -> int:
    left = 0
    hashmap = {}
    longest = 0
    for right in range(len(s)):
        char = s[right]
        if char in hashmap and hashmap[char] >= left:
            left = hashmap[char] + 1
        hashmap[char] = right
        longest = max(longest, right - left + 1)

    return longest


"""
s = 'abcabcbb'

1. char = a, hashmap = {a:0}, longest = max(0, 1) = 1
2. char = b, hashmap = {a:0, b:1}, longest = max(0, 1 - 0 + 1) = 2
3. char = c, hashmap = {a:0, b:1, c:2}, longest = max(2, 2 - 0 + 1) = 3
4. char = a, hashmap = {a:3, b:1, c:2}, left = 1, longest = max(3, 3 - 1 + 1) = 3
5. char = b, hashmap = {a:3, b:4, c:2}, left = 2, longest = max(3, 4 - 2 + 1) = 3
6. char = c, hashmap = {a:3, b:4, c:5}, left = 3, longest = max(3, 5 - 3 + 1) = 3
7. char = b, hashmap = {a:3, b:6, c:5}, left = 5, longest = max(3, 6 - 5 + 1) = 3
8. char = b, hashmap = {a:3, b:7, c:5}, left = 7, longest = max(3, 7 - 7 + 1) = 3
"""


if __name__ == "__main__":
    s = "abcabcbb"
    length_longest_substring(s)
