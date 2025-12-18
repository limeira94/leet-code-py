"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
"""

from typing import List


def max_area(height: List[int]) -> int:
    n = len(height)
    l = 0
    r = n - 1
    max_a = 0

    while l < r:
        w = r - l
        h = min(height[l], height[r])
        area = w * h
        max_a = max(max_a, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_a


def test_1():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert max_area(height) == 49


def test_2():
    height = [1, 1]
    assert max_area(height) == 1


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    max_area(height) == 49
