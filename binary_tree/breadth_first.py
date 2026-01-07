from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        left = self.left.val if self.left else None
        right = self.right.val if self.right else None
        return f"Node(val={self.val}, left={left}, right={right})"

    def __repr__(self):
        return self.__str__()


def breadth_first_value(root):
    if root is None:
        return []

    values = []
    queue = deque([root])

    while queue:
        current = queue.popleft(0)
        values.append(current.val)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return values


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

breadth_first_value(a)
