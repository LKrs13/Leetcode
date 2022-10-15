# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        
        def helper(node):
            nonlocal res
            
            if node is None:
                return 0
            
            left = 1 + helper(node.left)
            right = 1 + helper(node.right)
            
            if abs(left - right) > 1:
                res = False
            
            return max(left, right)
        
        helper(root)
        return res
            
            