from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# Time O(n) Space O(h) -> height is tree -> O(n)
def invertTreerec(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    
    root.left, root.right = root.right, root.left
    
    invertTree(root.left)
    invertTree(root.right)
    
    return root

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return False
    
    queue = deque([root])
    while queue:
        current = queue.popleft()
        current.left, current.right = current.right, current.left
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return root