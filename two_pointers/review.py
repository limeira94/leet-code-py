"""
s= "A man, a plan, a canal: Panama"
"""


def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        right -= 1
        left += 1
    return True


# s = "abc", t = "ahbgdc"
def is_subsequence(s: str, t: str) -> bool:
    if len(s) > len(t):
        return False
    i = 0
    for char in t:
        if char == s[i]:
            i += 1
    if i == len(s):
        return True
    return False


if __name__ == "__main__":
    s = "acb"
    t = "ahbgdc"
    is_subsequence(s, t)
