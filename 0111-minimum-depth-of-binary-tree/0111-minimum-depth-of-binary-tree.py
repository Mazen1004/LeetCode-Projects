# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if root.left is None and root.right is None:
            return 1
        
        if root.left is None:
            right = self.minDepth(root.right) + 1
            return right

        if root.right is None:
            left = self.minDepth(root.left) + 1
            return left
    
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        return min(left, right) + 1