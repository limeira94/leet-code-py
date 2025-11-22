"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
starting with word1. If a string is longer than the other, append the additional letters onto
the end of the merged string.
Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d
"""


# def mergeAlternately(word1: str, word2: str) -> str:
#     # Input: word1 = "abc", word2 = "pqr"
#     # Output: "apbqcr"
#     # 1. "ap"
#     # 2. "apbq"
#     # 3. "apbqcr"
#     merge = ""
#     limit = min(len(word1), len(word2))
#     for i in range(limit):
#         merge += word1[i] + word2[i]
#     merge += word1[limit:] + word2[limit:]
#     return merge

# O time complexity nesse caso seria O(n + m), e o espaço também
def mergeAlternately(word1: str, word2: str) -> str:
    result = "".join(a + b for a, b in zip(word1, word2))
    limit = min(len(word1), len(word2))
    result += word1[limit:] + word2[limit:]
    return result


def test_merge_1():
    word1 = "abc"
    word2 = "pqr"
    assert mergeAlternately(word1, word2) == "apbqcr"


def test_merge_2():
    word1 = "ab"
    word2 = "pqrs"
    assert mergeAlternately(word1, word2) == "apbqrs"


def test_merge_3():
    word1 = "abcd"
    word2 = "pq"
    assert mergeAlternately(word1, word2) == "apbqcd"
