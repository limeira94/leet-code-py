class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        right = self.right.val if self.right else None
        left = self.left.val if self.left else None
        return f"Node(val={self.val}, left={left}, right={right})"

    def __repr__(self):
        return self.__str__()


def depth_first_values(root):
    if root is None:
        return []

    summ = 0
    stack = [root]

    while stack:
        current = stack.pop()
        summ += current.val

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)

    return summ


a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(2)
f = Node(1)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


depth_first_values(a)
 