# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        def dfs(node):
            if not node:
                return
            
            left = dfs(node.left)
            values.append(node.val)
            right = dfs(node.right)

        values = []
        ans = 0
        dfs(root)
        mindiff = float("inf")
        for i in range(len(values)):
            if (mindiff > abs(values[i] - target)):
                mindiff = abs(values[i] - target)
                ans = values[i]
        
        return ans


        