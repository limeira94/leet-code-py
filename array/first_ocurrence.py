"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""


# Time complexity O(n*m) o M é o slice e o n cada iteração space complexity
# Space complexit O(1) pois o garbage collector consome a memória e logo em seguida troca para próxima mantendo o mesmo tamanho.
def first_ocurrence_str2(haystack: str, needle: str) -> int:
    len_n = len(needle)

    for i in range(len(haystack)):
        if haystack[i:len_n] == needle:
            return i
        len_n += 1
    return -1


def first_ocurrence_str(haystack: str, needle: str) -> int:
    m = len(needle)
    n = len(haystack)

    for i in range(n - m + 1):
        if haystack[i : i + m] == needle:
            return i
    return -1


def test_1():
    haystack = "sadbutsad"
    needle = "sad"
    assert first_ocurrence_str(haystack, needle) == 0


def test_2():
    haystack = "leetcode"
    needle = "leeto"
    assert first_ocurrence_str(haystack, needle) == -1


def test_3():
    haystack = "hello"
    needle = "ll"
    first_ocurrence_str(haystack, needle) == 2


if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"
    first_ocurrence_str(haystack, needle)
