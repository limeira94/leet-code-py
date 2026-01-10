from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


    def __repr__(self):
        right_val = self.right.val if self.right else None
        left_val = self.left.val if self.left else None
        return f"{self.val}"


# def same_tree(p, q):
#     if not p and not q:
#         return True
#     if (p and not q) or (q and not p):
#         return False

#     if p.val != q.val:
#         return False

#     print(f"p: {p.val}, q: {q.val}")
#     return same_tree(p.left, q.left) and same_tree(p.right, q.right)


def same_tree(p, q):
    queue = deque([(p, q)])

    while queue:
        node_p, node_q = queue.popleft()

        if node_p is None and node_q is None:
            continue
        if (not node_p or not node_q) or (node_p.val != node_q.val):
            return False

        queue.append((node_p.left, node_q.left))
        queue.append((node_p.right, node_q.right))
    return True


# queue = [(1, 1)] --> node_p, node_q = (1, 1)
# queue = [(2, 2), (3, 3)] --> node_p, node_q = (2, 2)
# queue = [(3, 3), (None, None), (None, None)]
# queue = [(3, 3)] --> node_p, node_q = (3, 3)
# queue = [(None, None), (None, None), (None, None)]
# queue = [(None, None), (None, None)] --> node_p, node_q = (None, None)
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)

a.left = b
b.right = c

x = TreeNode(1)
y = TreeNode(2)
z = TreeNode(3)

x.left = y
y.right = z

print(same_tree(a, x))
