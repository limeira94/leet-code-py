"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:

Input: arr = [1,2]
Output: false

Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
"""

from typing import List
from collections import Counter


def unique_occurrences(arr: List[int]) -> bool:
    hash_m = Counter(arr)

    values = hash_m.values()
    if len(values) == len(set(values)):
        return True
    return False


# Em relação ao O(n) as duas possuem o mesmo peso, agora se é possível melhorar em tempo de execução sim, daria para 
# verificar se o valor já está no set e parar caso esteja. O problema que o python o foor loop é gerado no proprio
# python, já o set e o count sao calculados pelo Cpython
def unique_ocurrences2(arr: List[int]) -> bool:
    counts = Counter(arr)
    seen = set()
    for count in counts.values():
        if count in seen:
            return False
        seen.add(count)
    return True


def test_1():
    arr = [1, 2, 2, 1, 1, 3]
    assert unique_occurrences(arr) is True


def test_2():
    arr = [1, 2]
    assert unique_occurrences(arr) is False


def test_3():
    arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    assert unique_occurrences(arr) is True
