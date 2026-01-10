from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        left_val = self.left.val if self.left else None
        right_val = self.right.val if self.right else None
        return f"val={self.val} left={left_val} right={right_val}"


# def symmetric_tree(root):
#     def same(root1, root2):
#         if not root1 and not root2:
#             return True

#         if (not root1 or not root2) or (root1.val != root2.val):
#             return False
#         print(root1.val, root2.val)
#         return same(root1.left, root2.right) and same(root1.right, root2.left)

#     return same(root, root)


def symmetric_tree(root):
    queue = deque([(root.left, root.right)])

    while queue:
        node_p, node_q = queue.popleft()

        if node_p is None and node_q is None:
            continue

        if (not node_p or not node_q) or (node_p.val != node_q.val):
            return False

        queue.append((node_p.left, node_q.right))
        queue.append((node_p.right, node_q.left))
    return True


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(2)
d = TreeNode(3)
e = TreeNode(4)
f = TreeNode(4)
g = TreeNode(3)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

print(symmetric_tree(a))
