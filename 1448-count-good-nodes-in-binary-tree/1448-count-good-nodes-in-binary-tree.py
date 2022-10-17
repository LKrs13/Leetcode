# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        
        def dfs(node, parentVal):
            nonlocal res
            
            if node is None:
                return
            
            if node.val >= parentVal:
                res += 1
                parentVal = node.val
            
            dfs(node.left, parentVal)
            dfs(node.right, parentVal)
        
        dfs(root, -float('inf'))
        
        return res