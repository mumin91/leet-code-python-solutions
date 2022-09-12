# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isMirror(self, right, left):
        if not right and not left:
            return True
        
        if not right or not left:
            return False
        
        if right.val != left.val:
            return False
        
        return self.isMirror(left.right, right.left) and self.isMirror(right.right, left.left)
        
        
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        return self.isMirror(root.right, root.left)