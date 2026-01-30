# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

# Time: 0(n) Space O(h) -> height tree == O(n)
def maxDepth(root):
    if not root:
        return 0
    
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    
    return 1 + max(left, right)

def maxDepth2(root):
    if not root:
        return 0
    queue = deque([root])
    level = 0
    
    while level:
        level_size = len(queue)
        
        for i in range(level_size):
            current = queue.popleft()
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        level += 1
        
    return level  
    