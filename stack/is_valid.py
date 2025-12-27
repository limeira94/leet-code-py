"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


def is_valid(s: str) -> bool:
    hashmap = {"]": "[", "}": "{", ")": "("}
    stack = []

    for char in s:
        if char not in hashmap:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            else:
                popped = stack.pop()
                if popped != hashmap[char]:
                    return False
    return not stack


def is_valid2(s: str) -> bool:
    hashmap = {"{": "}", "[": "]", "(": ")"}
    stack = []
    for char in s:
        if char in hashmap:
            stack.append(char)
        else:
            if stack == [] or char != hashmap[stack.pop()]:
                return False
    return True if stack == [] else False


"""
s = "[{()}]"

char = )
stack = ["[", "{"]
popped = ( -> hashmap['(']
"""


def test_1():
    s = "()"
    assert is_valid(s) is True


if __name__ == "__main__":
    s = "[{()}]"
    is_valid2(s)
